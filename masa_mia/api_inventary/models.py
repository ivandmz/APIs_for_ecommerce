from django.db import models

# Create your models here.

class Category(models.Model):
    """Every product has a category"""
    name = models.CharField(max_length=45,null=True, verbose_name = 'Nombre')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """The product that's going to be on sale"""
    name = models.CharField(max_length=45,null=True, verbose_name = 'Nombre')
    description = models.TextField(null=True, verbose_name = 'Descripción')
    price = models.FloatField(null=True, verbose_name= 'Precio')
    stock = models.PositiveBigIntegerField(null=True, verbose_name= 'Stock')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'Media/Productos')
    category = models.ForeignKey(Category, default='', null=True, blank=True, on_delete=models.CASCADE, related_name='Productos')


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    