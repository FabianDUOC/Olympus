from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    idRegion = models.AutoField(primary_key=True,verbose_name="Código de la Región")
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Región",null=False, blank=False)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True,verbose_name="Código de la Comuna")
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Comuna",null=False, blank=False)
    region = models.ForeignKey(Region,on_delete= models.CASCADE, verbose_name="Region de pertenencia")

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True,verbose_name="Código de la Dirección")
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Dirección",null=False, blank=False)
    comuna = models.ForeignKey(Comuna,on_delete= models.CASCADE, verbose_name="Comuna de pertenencia")
    idUsuario = models.IntegerField(unique=True)
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.nombre


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, nombre, apellidoPa, telefono, password, **other_fields):

        if not email:
            raise ValueError(_('Debe ingresar un correo'))

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre,
                          apellidoPa=apellidoPa, telefono=telefono, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre, apellidoPa, telefono, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, nombre, apellidoPa, telefono, password, **other_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nombre = models.CharField(max_length=100)
    apellidoPa = models.CharField(max_length=100)
    telefono = models.IntegerField()

    foto = models.ImageField(upload_to='users/', default='users/default.png', verbose_name="foto de perfil")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidoPa', 'telefono']

    def __str__(self):
        return f'{self.nombre} {self.apellidoPa}'
