from django.contrib import admin
from django.urls import path, include
from .views import index, iniciarSesion, cambiarClave, recuperarClave, registro, categoriaProducto, producto, editarCuenta, agregarProducto, registrarP, catalogoPoleras, catalogoPantalones, catalogoZapatillas, catalogoPolerones, catalogoChaquetas, cuenta, contacto, carrito, editarProducto, editarP, eliminarProducto, enviarCon, msjFooter

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path( 'iniciarSesion', iniciarSesion, name="iniciarSesion"),
    path( 'cambiarClave', cambiarClave, name="cambiarClave"),
    path( 'recuperarClave', recuperarClave, name="recuperarClave"),
    path( 'registro', registro, name="registro"),
    path( 'categoriaProducto', categoriaProducto, name="categoriaProducto"),
    path( 'producto/<int:id>', producto, name="producto"),
    path( 'editarCuenta', editarCuenta, name="editarCuenta"),
    path( 'agregarProducto', agregarProducto, name="agregarProducto"),
    path( 'registrarP', registrarP, name="registrarP"),
    path( 'catalogoPoleras', catalogoPoleras, name="catalogoPoleras"),
    path( 'catalogoPantalones', catalogoPantalones, name="catalogoPantalones"),
    path( 'catalogoZapatillas', catalogoZapatillas, name="catalogoZapatillas"),
    path( 'catalogoPolerones', catalogoPolerones, name="catalogoPolerones"),
    path( 'catalogoChaquetas', catalogoChaquetas, name="catalogoChaquetas"),
    path( 'cuenta', cuenta, name="cuenta"),
    path( 'contacto', contacto, name="contacto"),
    path( 'carrito', carrito, name="carrito"),
    path( 'editarProducto/<int:id>', editarProducto, name='editarProducto'),
    path( 'editarP/<int:id>', editarP, name='editarP'),
    path( 'eliminarProducto/<int:id>', eliminarProducto, name='eliminarProducto'),
    path( 'enviarCon', enviarCon, name="enviarCon"),
    path( 'msjFooter', msjFooter, name="msjFooter"),
]