
from django.urls import path, include
from .views import agregar_producto, eliminar_producto, restar_producto,limpiar_carrito

app_name = 'carrito'

urlpatterns = [
    path('agregar_producto/<int:idProducto>/', agregar_producto, name="agregar_producto"),
    path('eliminar_producto/<int:idProducto>/', eliminar_producto, name="eliminar_producto"),
    path('restar_producto/<int:idProducto>/', restar_producto, name="restar_producto"),
    path('limpiar_carrito', limpiar_carrito, name="limpiar_carrito")
    
]