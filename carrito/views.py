from django.shortcuts import render
from .carrito import Carrito
from core.models import Producto
from django.shortcuts import redirect
# Create your views here.
def agregar_producto(request, idProducto):
    carrito=Carrito(request)

    producto=Producto.objects.get(idProducto=idProducto)
    carrito.agregarProducto(producto=producto)
    return redirect(request.META.get('HTTP_REFERER'))

def eliminar_producto(request, idProducto):
    carrito=Carrito(request)

    producto=Producto.objects.get(idProducto=idProducto)
    carrito.eliminarProducto(producto=producto)
    return redirect(request.META.get('HTTP_REFERER'))

def restar_producto(request, idProducto):
    carrito=Carrito(request)

    producto=Producto.objects.get(idProducto=idProducto)
    carrito.restar_producto(producto=producto)
    return redirect(request.META.get('HTTP_REFERER'))

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect(request.META.get('HTTP_REFERER'))
    