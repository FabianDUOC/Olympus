from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from users.models import Comuna, Direccion, UserProfile

from .forms import UserLoginForm, UserSignUpForm


def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('core:index')
        else:
            messages.warning(request, 'Correo Electrónico o Contrasena inválida')
            return redirect('core:iniciarSesion')

    messages.error(request, 'Formulario Inválido')
    return redirect('core:iniciarSesion')


def signup_view(request):
    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        nombre = signup_form.cleaned_data.get('nombre')
        apellidoPa = signup_form.cleaned_data.get('apellidoPa')
        apellidoMa = signup_form.cleaned_data.get('apellidoMa')
        telefono = signup_form.cleaned_data.get('telefono')
        password = signup_form.cleaned_data.get('password')
        direccion = request.POST['direccion']
        comuna = request.POST['comuna']
        try:
            comuna2 = Comuna.objects.get(nombre = comuna)
            Direccion.objects.create(nombre = direccion, comuna=comuna2,email=email)
            user = get_user_model().objects.create(
                email=email,
                nombre=nombre,
                apellidoPa=apellidoPa,
                apellidoMa=apellidoMa,
                telefono=telefono,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('core:cuenta')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})


def logout_view(request):
    logout(request)
    return redirect('core:index')


@login_required(login_url='core:index')
def profile_view(request):
    return render(request, 'core:cuenta')


