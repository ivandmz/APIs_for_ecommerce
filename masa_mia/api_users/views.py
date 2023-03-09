from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers, AddressSerializers, UserDetailsSerializers
from .models import User, Address, UserDetails
from rest_framework import status
from django.http import Http404

# Create your views here.
class User_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Address_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        address = Address.objects.all()
        serializer = AddressSerializers(address, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Address_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializers(address)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializers(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserDetails_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        userDetails = UserDetails.objects.all()
        serializer = UserDetailsSerializers(userDetails, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return UserDetails.objects.get(pk=pk)
        except UserDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userDetails = self.get_object(pk)
        serializer = UserDetailsSerializers(userDetails)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userDetails = self.get_object(pk)
        serializer = UserDetailsSerializers(userDetails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userDetails = self.get_object(pk)
        userDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)