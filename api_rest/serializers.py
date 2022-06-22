from rest_framework import serializers
from core.models import Categoria, Producto
from users.models import Region, Comuna

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','descCorta','descLarga','precio','stock','foto','categoria','estatus']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreC']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['idRegion','nombre']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['idComuna','nombre']