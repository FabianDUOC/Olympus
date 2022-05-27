from django.shortcuts import render, redirect
from .models import Producto, Categoria

# Create your views here.
def index(request):
    return render(request,'core/index.html')
    
def iniciarSesion(request):
    return render(request,'core/iniciarSesion.html')

def cambiarClave(request):
    return render(request,'core/cambiarClave.html')

def recuperarClave(request):
    return render(request,'core/recuperarClave.html')

def registro(request):
    return render(request,'core/registro.html')

def categoriaProducto(request):
    return render(request,'core/categoriaProducto.html')

def producto(request):
    return render(request,'core/producto.html')

def editarCuenta(request):
    return render(request,'core/editarCuenta.html')

def agregarProducto(request):
    categorias = Categoria.objects.all()
    contexto = {"categoria_p":categorias}
    return render(request,'core/agregarProducto.html',contexto)

def registrarP(request):
    return redirect('agregarProducto')

def catalogoPoleras(request):
    return render(request,'core/catalogoPoleras.html')

def catalogoPantalones(request):
    return render(request,'core/catalogoPantalones.html')

def catalogoZapatillas(request):
    return render(request,'core/catalogoZapatillas.html')

def catalogoPolerones(request):
    return render(request,'core/catalogoPolerones.html')

def catalogoChaquetas(request):
    return render(request,'core/catalogoChaquetas.html')

def cuenta(request):
    return render(request,'core/cuenta.html')