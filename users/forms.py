from django import forms
from users.models import Comuna, Region


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Ingresar Correo Electrónico'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Ingresar Contraseña'
        })
    )


class UserSignUpForm(forms.Form):
    # Campos del Formulario
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupEmail',
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Ingresar Correo Electrónico'
            }
        )
    )

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'nombre',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Ingresar Nombre'
            }
        ))

    apellidoPa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'apellidoPa',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Ingresar Primer Apellido'
            }
        ))
    
    apellidoMa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'apellidoMa',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Ingresar Segundo Apellido'
            }
        ))

    direccion = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'direccion',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Ingresar Dirección'
            }
        ))

    region = forms.ModelChoiceField( 
        queryset=Region.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'region',
                'class': 'form-select',
            }
        ))

    comuna = forms.ModelChoiceField( 
        queryset=Comuna.objects.none(),
        widget=forms.Select(
            attrs={
                'id': 'comuna',
                'class': 'form-select',
            }
        ))

    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'telefono',
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Ingresar Número de Teléfono'
            }
        ))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave1',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Ingresar Contraseña'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave2',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Repetir Contraseña'
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']