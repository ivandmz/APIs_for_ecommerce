from django.urls import path
from .views import Ticket_APIView, Ticket_APIView_Detail, Sale_APIView, Sale_APIView_Detail, Charge_APIView, Charge_APIView_Detail

app_name = 'api_sales'

urlpatterns = [
    path('ticket',  Ticket_APIView.as_view(), name='tickets_lista'), 
    path('ticket/<int:pk>/', Ticket_APIView_Detail.as_view(), name='ticket_detalle'),
    path('sale',  Sale_APIView.as_view(), name='ventas_lista'), 
    path('sale/<int:pk>/', Sale_APIView_Detail.as_view(), name='venta_detalle'),
    path('charge',  Charge_APIView.as_view(), name='cobros_lista'), 
    path('charge/<int:pk>/', Charge_APIView_Detail.as_view(), name='cobro_detalle'),
]