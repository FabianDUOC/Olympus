from asyncio.windows_events import NULL
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import check_password

from users.models import Comuna, Direccion, UserProfile

from .forms import UserLoginForm, UserSignUpForm


def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email').lower()
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('core:index')
        else:
            messages.warning(request, 'Correo Electrónico o Contraseña inválida')
            return redirect('core:iniciarSesion')

    messages.error(request, 'Formulario Inválido')
    return redirect('core:iniciarSesion')


def signup_view(request):
    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email').lower()
        nombre = signup_form.cleaned_data.get('nombre')
        apellidoPa = signup_form.cleaned_data.get('apellidoPa')
        telefono = signup_form.cleaned_data.get('telefono')
        password = signup_form.cleaned_data.get('password')
        direccion = request.POST['direccion']
        comuna = request.POST['comuna']

        try:
            valid = UserProfile.objects.get(email = email)
        except:
            valid = NULL
        try:
            if valid is not NULL:
                messages.warning(request, 'correo ya registrado') 
                return redirect('core:registro')
            else:

                user = get_user_model().objects.create(
                    email=email,
                    nombre=nombre,
                    apellidoPa=apellidoPa,
                    telefono=telefono,
                    password=make_password(password),
                    is_active=True
                )
                idUser = UserProfile.objects.latest('id')
                comuna2 = Comuna.objects.get(nombre = comuna)
                Direccion.objects.create(nombre = direccion, comuna=comuna2,idUsuario=idUser.id,email=email)
                login(request, user)
                messages.success(request, 'Cuenta registrada')
                return redirect('core:cuenta')

        except Exception as e:
            print(e)
            messages.warning(request, 'Ha ocurrido un error')
            return redirect('core:registro')


def logout_view(request):
    logout(request)
    return redirect('core:index')


@login_required(login_url='core:index')
def profile_view(request):
    return render(request, 'core:cuenta')


@login_required(login_url='core:index')
def profile_change_password(request, id):
    u = UserProfile.objects.get(id = id)
    claveActual = request.POST['claveActual']
    claveANu1 = request.POST['claveNueva1']

    pass_valida = check_password(claveActual, u.password)

    if not pass_valida:
        messages.warning(request, 'Contraseña actual no valida')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        u.password = (make_password(claveANu1))
        u.save()
        user = authenticate(request, email=u.email, password=claveANu1)
        if user is not None:
            login(request, user)
            messages.success(request, 'Contraseña Actualizada')
            return redirect('core:cuenta')
        else:
            messages.warning(request, 'Ha ocurrido un error')
            return redirect('core:iniciarSesion')
        


