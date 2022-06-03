import random
import string

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, nombre, apellidoPa, apellidoMa, direccion, telefono, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre,
                          apellidoPa=apellidoPa, apellidoMa=apellidoMa, direccion=direccion, telefono=telefono, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre, apellidoPa, apellidoMa, direccion, telefono, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, nombre, apellidoPa, apellidoMa, direccion, telefono, password, **other_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nombre = models.CharField(max_length=100)
    apellidoPa = models.CharField(max_length=100)
    apellidoMa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    telefono = models.IntegerField()


    foto = models.ImageField(upload_to='users/', default='users/default.png', verbose_name="foto de perfil")
    
    slug = models.SlugField(max_length=255, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidoPa','apellidoMa','direccion','telefono']

    def __str__(self):
        return f'{self.nombre} {self.apellidoPa}'

    def get_absolute_url(self):
        return reverse('users:user_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.email)
        super(UserProfile, self).save(*args, **kwargs)