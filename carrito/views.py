from django.shortcuts import render
from .carrito import Carrito
from core.models import Producto
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def agregar_producto(request, idProducto):
    carrito=Carrito(request)

    producto=Producto.objects.get(idProducto=idProducto)
    carrito.agregarProducto(producto=producto)
    messages.success(request, 'Producto Agregado al carrito')
    return redirect(request.META.get('HTTP_REFERER'))

def agregar_producto_varios(request, idProducto):
    numero = request.POST['formCantidad']
    numero = int(numero)
    print(numero)
    print(type(numero))
    
    for i in range(numero):
        print("1********")
        carrito=Carrito(request)
        print("*2*******")
        producto=Producto.objects.get(idProducto=idProducto)
        print("***3*****")
        carrito.agregarProducto(producto=producto)
        print("****4****")
    
    messages.success(request, 'Producto Agregado al carrito')
    return redirect(request.META.get('HTTP_REFERER'))

def añadir_producto(request, idProducto):
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
    messages.success(request, 'Carrito Vaciado')
    return redirect(request.META.get('HTTP_REFERER'))
    