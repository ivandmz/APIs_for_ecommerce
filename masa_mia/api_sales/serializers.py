from rest_framework import serializers
from api_sales.models import Ticket, Sale, Charge 

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket  
        fields = ("products_amount","total_sale","products")

class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale  
        fields = ("num_sale","date_sale","installments_interval","initial_deposit","installments_amount","ticket", "user_details")

class ChargeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Charge  
        fields = ("payment","historical_balance","payment_date","user_details","sale")