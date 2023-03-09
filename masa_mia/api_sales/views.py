from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TicketSerializers, SaleSerializers, ChargeSerializers
from .models import Ticket, Sale, Charge
from rest_framework import status
from django.http import Http404

# Create your views here.
class Ticket_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        ticket = Ticket.objects.all()
        serializer = TicketSerializers(ticket, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TicketSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Ticket_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializers(ticket)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer =TicketSerializers(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Sale_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        sale = Sale.objects.all()
        serializer = SaleSerializers(sale, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SaleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sale_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sale = self.get_object(pk)
        serializer = SaleSerializers(sale)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sale = self.get_object(pk)
        serializer = SaleSerializers(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sale = self.get_object(pk)
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Charge_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        charge = Charge.objects.all()
        serializer = ChargeSerializers(charge, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChargeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Charge_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Charge.objects.get(pk=pk)
        except Charge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        charge = self.get_object(pk)
        serializer = ChargeSerializers(charge)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        charge = self.get_object(pk)
        serializer = ChargeSerializers(charge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        charge = self.get_object(pk)
        charge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)