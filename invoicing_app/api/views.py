
from django.http.response import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InvoiceProduct,Invoice
from .serialzers import InvoiceSerializer , InvoiceProductSerializer

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

class InvoiceList(APIView):
    def get(self,request):
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self,request,response):
        invoice = Invoice.objects.create(request.data)
        serializer= InvoiceSerializer(data=invoice)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors(Http404))
        
        
