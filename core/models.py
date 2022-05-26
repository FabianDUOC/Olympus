from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="Código de la Categoría")
    nombreC = models.CharField(max_length=30, verbose_name="Nombre de la Categoría",null=False, blank=False)

    def __str__(self):
        return self.nombreC

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='código del Producto')
    nombreProducto = models.CharField(max_length=30, verbose_name='Nombre del Producto')
    descCorta = models.CharField(max_length=30, verbose_name='Descripción Corta del Producto')
    descLarga = models.CharField(max_length=200, verbose_name='Descripción Detallada del Producto')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    stock = models.IntegerField(verbose_name='Cantidad en Stock del Producto')
    foto = models.ImageField(upload_to="core", null= True)

    def __str__(self):
        return self.nombreProducto