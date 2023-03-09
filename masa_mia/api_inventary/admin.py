from django.contrib import admin
from .models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","description","price","stock","image","category") # campos q aparecen
    fields = ['image', ('name','category'), 'price','description','stock',] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
    search_fields = ('name','category','price',)
    list_filter = ("category","price",)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)