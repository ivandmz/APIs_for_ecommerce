from django.urls import path
from .views import Category_APIView, Category_APIView_Detail, Product_APIView, Product_APIView_Detail

app_name = 'api_inventary'

urlpatterns = [
    path('product',  Product_APIView.as_view(), name='productos_lista'), 
    path('product/<int:pk>/', Product_APIView_Detail.as_view(), name='producto_detalle'),
    path('category',  Category_APIView.as_view(), name='categorias_lista'), 
    path('category/<int:pk>/', Category_APIView_Detail.as_view(), name='categoria_detalle'),
]