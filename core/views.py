from django.shortcuts import render, redirect
from .models import Producto, Categoria

# Create your views here.
def index(request):
    return render(request,'core/index.html')
    
def iniciarSesion(request):
    return render(request,'core/iniciarSesion.html')

def CambiarClave(request):
    return render(request,'core/cambiarClave.html')

def recuperarClave(request):
    return render(request,'core/recuperarClave.html')

def registro(request):
    return render(request,'core/registro.html')

def CategoriaProducto(request):
    return render(request,'core/categoriaProducto.html')

def Producto(request):
    return render(request,'core/producto.html')

def EditarCuenta(request):
    return render(request,'core/editarCuenta.html')

def AgregarProducto(request):
    categorias = Categoria.objects.all()
    contexto = {"categoria_p":categorias}
    return render(request,'core/agregarProducto.html',contexto)

def registrarP(request):
    chip_m = request.POST['chip']
    nombre_m = request.POST['nombre']
    edad_m = request.POST['edad']
    raza_m = request.POST['raza']
    img_foto = request.FILES['foto_m']
    #obtener el registro completo de la raza
    raza_c = Raza.objects.get(codigo = raza_m)

    #insert
    Mascota.objects.create(codigoChip = chip_m, nombreMascota = nombre_m, edadMascota = edad_m, foto = img_foto , raza = raza_c) 

    messages.success(request,'Mascota Registrada')

    return redirect('formulario')

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