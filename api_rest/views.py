from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api_rest.serializers import CategoriaSerializer, ComunaSerializer, ProductoSerializer, RegionSerializer
from core.models import Categoria, Producto
from users.models import Comuna, Region


@csrf_exempt

# METODOS PARA PRODUCTOS
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarProducto(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlProducto(request,idP):
    try:
        p = Producto.objects.get(idProducto = idP)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(p)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(p,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listaProductos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto,many=True)
        return Response(serializer.data)

# METODOS PARA CATEGORIAS
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarCategoria(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listaCategorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria,many=True)
        return Response(serializer.data)


# METODOS PARA REGION
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listaRegiones(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region,many=True)
        return Response(serializer.data)

# METODOS PARA Comuna
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listaComunas(request):
    if request.method == 'GET':
        comuna = Comuna.objects.all()
        serializer = ComunaSerializer(comuna,many=True)
        return Response(serializer.data)