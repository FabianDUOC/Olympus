from django.contrib import admin
from .models import Categoria, Producto, Estatus

# Register your models here.
# Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Estatus)
admin.site.register(Producto)
