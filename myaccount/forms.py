from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.db import transaction

from auth_bangsal.models import Bangsal

from .models import ProfilUser, Users


class UserSignUpForm(UserCreationForm):
    PENDIDIKANLEVEL = (
        ('', '-----------'),
        ('SD', 'SD'),
        ('SMP', 'SMP'),
        ('SMA', 'SMA'),
        ('Diploma', 'Diploma'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
    )

    
    JABATANLEVEL = (
        ('', '---------'),
        ('Kepala Instalasi', 'Kepala Instalasi'),
        ('Tenaga Kesehatan', 'Tenaga Kesehatan'),
        ('Administrator', 'Administrator'),
        ('Lainnya', 'Lainnya'),
    )

    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    no_hp = forms.CharField(required=True)
    alamat = forms.CharField(widget=forms.Textarea)
    pendidikan = forms.ChoiceField(required=True, choices=PENDIDIKANLEVEL)
    jabatan = forms.ChoiceField(required=True, choices=JABATANLEVEL)
    # instalasi = forms.ModelChoiceField(required=True, queryset=Bangsal.objects.using('auth_db').all())
    # foto = forms.ImageField(required=True)
   

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("email", 'first_name', 'last_name')

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_admin = True
        user.save()
        profil = ProfilUser.objects.using('auth_db').create(user=user)
        profil.no_hp = self.cleaned_data.get('no_hp')
        profil.alamat = self.cleaned_data.get('alamat')
        profil.pendidikan = self.cleaned_data.get('pendidikan')
        profil.jabatan = self.cleaned_data.get('jabatan')
        profil.instalasi = self.cleaned_data.get('instalasi')
        # profil.foto = self.cleaned_data.get('foto')
        profil.save()
        return user


class UpdateUser(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name']


class UpdateProfil(forms.ModelForm):
    class Meta:
        model = ProfilUser
        fields = ['no_hp', 'alamat', 'pendidikan', 'jabatan', 'foto']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Users.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email has taken')
        return email

    def clean_password2(self):
        # check taht the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. include all the required
    fields, plus a repeated password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        users = super(UserAdminCreationForm, self).save(commit=False)
        users.set_password(self.cleaned_data["password1"])
        if commit:
            users.save()
        return users


class UserAdminChangeForm(forms.ModelForm):
    """
    A Form for updating users. Include all the fields on the user,
    but replaces the password field with admin's password hash display
    field
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = Users
        fields = ('email', 'password', 'is_active')

    def clean_password(self):

        # Regardless of what the user provides, return the initial value
        # This is done here, rather than on the field, because the
        # field does not have acces to the initial value
        return self.initial['password']
