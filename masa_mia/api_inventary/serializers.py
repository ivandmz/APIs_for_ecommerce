from rest_framework import serializers
from api_inventary.models import Category, Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category  
        fields = ("name",)

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product  
        fields = ("name","description","price","stock","image","category")