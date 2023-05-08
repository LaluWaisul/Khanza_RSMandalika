from django.urls import path
from .views import LoginAPI, loginporda, RegisterPorda, logout_view, ProfilView, EditProfil, GantiPasswordView
from knox import views as knox_views


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login_view'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    
    path('', loginporda, name='login'),
    path('registrasi-user/', RegisterPorda.as_view(), name='register'),
    path('signout/', logout_view, name='logout'),
    path('profil/', ProfilView.as_view(), name='profil_view'),
    path('editprofil/<int:id>/', EditProfil.as_view(), name='edit_profil'),
    path('password/', GantiPasswordView.as_view(
        template_name='update_pass.html'), name='edit_pass')
]
