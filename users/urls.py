from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'), # Iniciar Sesión
    path('profile/', views.profile_view, name='profile'), # Ver Perfil de Usuario
    path('signup/', views.signup_view, name='signup'), # Registrar Usuario
    path('logout/', views.logout_view, name='logout'), # Cerrar Sesión
    path('changePassword/<int:id>', views.profile_change_password, name='changePassword') # cambiar contraseña
]