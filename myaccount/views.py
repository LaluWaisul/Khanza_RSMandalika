from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from .models import Users, Profil
from .forms import UserSignUpForm, UpdateProfil, UpdateUser

# Create your views here.


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView


# class LoginView(KnoxLoginView):
#     authentication_classes = [BasicAuthentication]

class LoginAPI(APIView):
    serializer_class = LoginSerializer
    permission_classes = [
        AllowAny
    ]
    # authentication_classes = (knox.auth.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        datauser = UserSerializer(user).data
        _, token = AuthToken.objects.create(user=user)
        return Response({
            "id": token,
            "firts_name": datauser["first_name"],
            "last_name": datauser["last_name"],
            "email": datauser["email"],
        })
        

def loginporda(request):
    userlogin = request.user.is_authenticated
    # print(userlogin)
    if userlogin:
        return redirect(reverse('auth_mutu:dashboard_view'))
    else:

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('auth_mutu:dashboard_view'))
                else:
                    messages.error(
                        request, 'Username atau Password Salah')
            else:
                messages.error(
                    request, "Username atau Password Salah")

        return render(request, 'login.html', context={'form': AuthenticationForm()})


class RegisterPorda(CreateView):
    model = Users
    form_class = UserSignUpForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('auth_mutu:dashboard_view'))


def logout_view(request):
    logout(request)
    return redirect('/')


class ProfilView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    template_name = 'profil.html'
    model = Users

    def get(self, *args, **kwargs):
        id_user = self.request.user.id
        # print(id_user)
        user = self.model.objects.using('auth_db').get(id=id_user)
        profil = Profil.objects.using('auth_db').get(user__id=id_user)

        context = {
            'user': user,
            'profil': profil,
            'contact': 'contact',
        }
        return render(self.request, self.template_name, context)


class EditProfil(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    template_name = 'update_profil.html'
    model = Users

    def get(self, *args, **kwargs):

        u_form = UpdateUser(instance=self.request.user)
        p_form = UpdateProfil(instance=self.request.user.profil_user)
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'contact': 'contact',
        }
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        u_form = UpdateUser(self.request.POST,
                            instance=self.request.user)
        p_form = UpdateProfil(
            self.request.POST, self.request.FILES, instance=self.request.user.profil_user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(self.request, 'Profil anda telah di update!!')

        context = {
            'p_form': p_form,
            'u_form': u_form,
            'contact': 'contact',
        }
        return render(self.request, self.template_name, context)


class GantiPasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('myaccount:profil_view')
