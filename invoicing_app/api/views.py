
from django.http.response import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, InvoiceProduct,Invoice
from .serialzers import CompanySerializer, InvoiceSerializer , InvoiceProductSerializer
from rest_framework import serializers, status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'EndPoint':'/invoces/',
            'method':'GET',
            'description':'return a list of invoices'
        }
    ]
    return Response(routes)

class InvoiceListView(APIView):
    def get(self,request):
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self,request,response):
        invoice = Invoice.objects.create(request.data)
        serializer= InvoiceSerializer(data=invoice)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors(Http404))

class InvoiceView(APIView):

    def get_object(self,pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404
    
    def get(self,request,pk, format=None):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    
    def put(self,request,pk):
        invoice = self.get_object(pk)
        serializer= InvoiceSerializer(invoice,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors(Http404))
    
    def delete(self, request, pk, format=None):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class CompanyListView(APIView):      

    def get(self,request):
        invoice = Company.objects.all()
        serializer = CompanySerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self,request,response):
        invoice = Company.objects.create(request.data)
        serializer= CompanySerializer(data=invoice)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors(Http404))

class CompanyView(APIView):
    def get_object(self,pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        company = self.get_object(pk)
        serializer= CompanySerializer(company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors(Http404))
    
    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        