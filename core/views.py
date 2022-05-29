from django.shortcuts import render, redirect
from .models import Estatus, Producto, Categoria, Categoria
from django.contrib import messages

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
    nombre = request.POST['nombreProducto']
    descripcionC = request.POST['descripcionCorta']
    descripcionL = request.POST['descripcionDetallada']
    precio = request.POST['precioP']
    stock = request.POST['cantidad']
    foto = request.FILES['fotoInput']
    categoria = request.POST['categoria']

    categoria2 = Categoria.objects.get(idCategoria = categoria)

    estatus = Estatus.objects.get(idEstatus = 1)

    Producto.objects.create(nombreProducto = nombre, descCorta = descripcionC, descLarga = descripcionL, precio = precio, stock = stock, foto = foto, categoria = categoria2, estatus = estatus)
    messages.success(request,'Mascota Registrada')
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
    id_categoria = Categoria.objects.get(idCategoria = 1)
    chaquetas = Producto.objects.filter(categoria = id_categoria) #Seleccionar todas las chaquetas
    contexto = {"chaquetas":chaquetas}
    return render(request,'core/catalogoChaquetas.html',contexto)

def cuenta(request):
    return render(request,'core/cuenta.html')