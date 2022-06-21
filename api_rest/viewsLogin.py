from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    correo = data['email']
    clave = data['password']
    try:
        email1 = get_user_model().objects.get(email = correo)

    except :
        return Response("Datos Invalidos")

    pass_valida = check_password(clave, email1.password)

    if not pass_valida:
        return Response("Datos Invalidos")
    
    token, created = Token.objects.get_or_create(user = email1)
    return Response(token.key)
