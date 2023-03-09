from django.urls import path
from .views import *

app_name = 'api_users'

urlpatterns = [
    path('user/', User_APIView.as_view(), name='usuarios_lista'),
    path('user/<int:pk>/', User_APIView_Detail.as_view(), name='usuario_detalle'),
    path('address/', Address_APIView.as_view(), name='direcciones_lista'),
    path('address/<int:pk>/', Address_APIView_Detail.as_view(), name='direccion_detalle'),
    path('userDetails/', UserDetails_APIView.as_view(), name='detalles_usuarios_lista'),
    path('userDetails/<int:pk>/', UserDetails_APIView_Detail.as_view(), name='detalles_usuario_detalle'),
]