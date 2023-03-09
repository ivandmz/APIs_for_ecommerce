from rest_framework import serializers
from api_users.models import User, Address, UserDetails

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User  
        exclude = ('created',)

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address  
        fields = ("address_line1","address_line2","city","province","region")

class UserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ("first_name","second_name","last_name","second_last_name","doc_type", "doc_number","telephone_number", "user", "address")
        