from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
        })
    )


class UserSignUpForm(forms.Form):
    # Campos del Formulario
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupEmail',
                'type': 'email',
                'class': 'form-control'
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
                'class': 'form-control'
            }
        ))
    
    apellidoMa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'apellidoMa',
                'type': 'text',
                'class': 'form-control'
            }
        ))

    direccion = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'direccion',
                'type': 'text',
                'class': 'form-control'
            }
        ))

    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'telefono',
                'type': 'number',
                'class': 'form-control'
            }
        ))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave1',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave2',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']