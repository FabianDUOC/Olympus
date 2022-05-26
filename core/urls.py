from django.contrib import admin
from django.urls import path, include
from .views import index, iniciarSesion, CambiarClave, recuperarClave, registro, CategoriaProducto, Producto, EditarCuenta, AgregarProducto, registrarP, catalogoPoleras, catalogoPantalones, catalogoZapatillas, catalogoPolerones, catalogoChaquetas, cuenta

urlpatterns = [
    path('', index, name="index"),
    path( 'iniciarSesion', iniciarSesion, name="iniciarSesion"),
    path( 'cambiarClave', CambiarClave, name="cambiarClave"),
    path( 'recuperarClave', recuperarClave, name="recuperarClave"),
    path( 'registro', registro, name="registro"),
    path( 'categoriaProducto', CategoriaProducto, name="categoriaProducto"),
    path( 'producto', Producto, name="producto"),
    path( 'editarCuenta', EditarCuenta, name="editarCuenta"),
    path( 'agregarProducto', AgregarProducto, name="agregarProducto"),
    path( 'registrarP', registarP, name="registarP"),
    path( 'catalogoPoleras', catalogoPoleras, name="catalogoPoleras"),
    path( 'catalogoPantalones', catalogoPantalones, name="catalogoPantalones"),
    path( 'catalogoZapatillas', catalogoZapatillas, name="catalogoZapatillas"),
    path( 'catalogoPolerones', catalogoPolerones, name="catalogoPolerones"),
    path( 'catalogoChaquetas', catalogoChaquetas, name="catalogoChaquetas"),
    path( 'cuenta', cuenta, name="cuenta"),
]