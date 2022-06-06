from email import message
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Estatus, Producto, Categoria, Categoria
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from users.models import Direccion, UserProfile

from users.models import Comuna, Region, UserProfile
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#from context_processors import login_user

# Create your views here.
def index(request):
    return render(request,'core/index.html')
    
def iniciarSesion(request):
    return render(request,'core/iniciarSesion.html')

def cambiarClave(request):
    return render(request,'core/cambiarClave.html')

def recuperarClave(request):
    return render(request,'core/recuperarClave.html')

def categoriaProducto(request):
    return render(request,'core/categoriaProducto.html')

def producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    contexto = {"producto":producto}  
    return render(request,'core/producto.html', contexto)

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
    messages.success(request,'Producto Agregado')
    return redirect('core:agregarProducto')

def catalogoChaquetas(request):
    id_categoria = Categoria.objects.get(idCategoria = 1)
    chaquetas = Producto.objects.filter(categoria = id_categoria, stock__gte = 1, estatus=1) #Seleccionar todas las chaquetas
    contexto = {"chaquetas":chaquetas}
    return render(request,'core/catalogoChaquetas.html', contexto)

def catalogoPantalones(request):
    id_categoria = Categoria.objects.get(idCategoria = 2)
    pantalones = Producto.objects.filter(categoria = id_categoria, stock__gte = 1, estatus=1) #Seleccionar todos los pantalones
    contexto = {"pantalones":pantalones}
    return render(request,'core/catalogoPantalones.html', contexto)

def catalogoPoleras(request):
    id_categoria = Categoria.objects.get(idCategoria = 3)
    poleras = Producto.objects.filter(categoria = id_categoria, stock__gte = 1, estatus=1) #Seleccionar todas las poleras
    contexto = {"poleras":poleras}
    return render(request,'core/catalogoPoleras.html', contexto)

def catalogoPolerones(request):
    id_categoria = Categoria.objects.get(idCategoria = 4)
    polerones = Producto.objects.filter(categoria = id_categoria, stock__gte = 1, estatus=1) #Seleccionar todos los polerones
    contexto = {"polerones":polerones}
    return render(request,'core/catalogoPolerones.html', contexto)

def catalogoZapatillas(request):
    id_categoria = Categoria.objects.get(idCategoria = 5)
    zapatillas = Producto.objects.filter(categoria = id_categoria, stock__gte = 1, estatus=1) #Seleccionar todas las zapatillas
    contexto = {"zapatillas":zapatillas}
    return render(request,'core/catalogoZapatillas.html', contexto)

def carrito(request):
    return render(request,'core/carrito.html')

def contacto(request):

    return render(request,'core/contacto.html')

def enviarCon(request):

    asunto = request.POST['asunto']
    mensaje = request.POST['mensaje']+ '\r\n' + 'Nombre De Contacto: ' + request.POST['nombre'] + ' Correo De Contacto: ' + request.POST['email']
    emisor =settings.EMAIL_HOST_USER
    receptor =['lu.morgado@duocuc.cl', 'fa.marileo@duocuc.cl']
    
    send_mail(asunto, mensaje, emisor, receptor)
    messages.success(request,'Mensaje Enviado')
    return redirect('core:contacto')

def editarProducto(request, id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(idProducto = id)
    contexto = {"producto":producto, "categoria_p":categorias}  
    return render(request, 'core/editarProducto.html', contexto)

def editarP(request, id):
    nombre = request.POST['nombreProducto']
    descripcionC = request.POST['descripcionCorta']
    descripcionL = request.POST['descripcionDetallada']
    precio = request.POST['precioP']
    stock = request.POST['cantidad']

    categoria = request.POST['categoria']

    try:

        categoria2 = Categoria.objects.get(idCategoria = categoria)

    # obtener el registro de la base de datos
        producto = Producto.objects.get(idProducto = id)

    # reemplazar valores en el registro
        producto.nombreProducto = nombre
        producto.descCorta = descripcionC
        producto.descLarga = descripcionL
        producto.precio = precio
        producto.stock = stock
        producto.categoria = categoria2

        foto = request.FILES['fotoInput']
        producto.foto = foto
    except:
        foto = "No hay cambio"

    #update
    producto.save() 
    messages.success(request, 'Producto modificado')
    return redirect('core:editarProducto',id)

def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto = id)
    estatus = Estatus.objects.get(idEstatus = 2)
    
    producto.estatus = estatus
    producto.save()
    messages.success(request, 'Producto eliminado')
    if producto.categoria.idCategoria == 1:
        return redirect('core:catalogoChaquetas')
    elif producto.categoria.idCategoria == 2:
        return redirect('core:catalogoPantalones')
    elif producto.categoria.idCategoria == 3:
        return redirect('core:catalogoPoleras')
    elif producto.categoria.idCategoria == 2:
        return redirect('core:catalogoPolerones')
    elif producto.categoria.idCategoria == 2:
        return redirect('core:catalogoZapatillas')

def msjFooter(request):

    asunto = 'Suscripcion Realizada'
    mensaje = 'Usted se ha suscrito correctamente, Pronto le llegaran las nuevas ofertas'
    emisor =settings.EMAIL_HOST_USER
    rec = request.POST['emailF']
    receptor = [rec]
    pagAnt =request.POST['pagAnt']
    send_mail(asunto, mensaje, emisor, receptor)
    messages.success(request,'Suscripcion Realizada')
    
   
    return redirect(pagAnt)

def editarUsuario(request, id):
    nombre = request.POST['nombre']
    apellidoPa = request.POST['apellidoPa']
    apellidoMa = request.POST['apellidoMa']
    telefono = request.POST['telefono']

    try:
        usuario = UserProfile.objects.get(id = id)
        usuario.nombre = nombre
        usuario.apellidoPa = apellidoPa
        usuario.apellidoMa = apellidoMa
        usuario.telefono = telefono

        foto = request.FILES['fotoInput']
        usuario.foto = foto

    except:
        foto = "No hay cambio"

    #update de los campos de usuario     
    usuario.save()

    try:
        direc = request.POST['direccion']
        comuna = request.POST['comuna']
        direccionUsuario = Direccion.objects.get(idUsuario = id)
        comuna1 = Comuna.objects.get(nombre = comuna)
        direccionUsuario.nombre = direc
        direccionUsuario.comuna = comuna1
        direccionUsuario.save()
    except:
        None
    #update de los campos de direccion  
    messages.success(request,'Cambios Guardados')
    return redirect('core:cuenta')


@method_decorator(csrf_exempt, name='dispatch')
class registroFormView(TemplateView):
    template_name = 'core/registro.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_comuna_id':
                data = []
                for i in Comuna.objects.filter(region= request.POST['id']):
                    data.append({'id': i.idComuna, 'nombre': i.nombre })
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = 'Ha ocurrido un error'
        return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class editarCuentaFormView(TemplateView):
    template_name = 'core/editarCuenta.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_comuna_id':
                data = []
                for i in Comuna.objects.filter(region= request.POST['id']):
                    data.append({'id': i.idComuna, 'nombre': i.nombre })
                return JsonResponse(data, safe=False)
            
            if action == 'buscar_direccion':
                data = []
                direccion = Direccion.objects.get(email = request.POST['email'])
                comuna = Comuna.objects.get(nombre = direccion.comuna)
                region = Region.objects.get(nombre = comuna.region)
                return JsonResponse({'direccionU':direccion.nombre, 'comunaU':comuna.idComuna, 'regionU':region.idRegion })
            else:
                data['error'] = 'Ha ocurrido un error'
                return JsonResponse(data, safe=False)
        except:
            data['error'] = 'Ha ocurrido un error'
            return JsonResponse(data, safe=False)


def cuenta(request):
    return render(request,'core/cuenta.html')

@method_decorator(csrf_exempt, name='dispatch')
class cuentaView(TemplateView):
    template_name = 'core/cuenta.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_direccion':
                data = []
                direccion = Direccion.objects.get(email = request.POST['email'])
                comuna = Comuna.objects.get(nombre = direccion.comuna)
                region = Region.objects.get(nombre = comuna.region)
                return JsonResponse({'direccionU':direccion.nombre, 'comunaU':comuna.nombre, 'regionU':region.nombre })
            else:
                data['error'] = 'Ha ocurrido un error'
                return JsonResponse(data, safe=False)
        except:
            data['error'] = 'Ha ocurrido un error'
            return JsonResponse(data, safe=False)