
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['GET'])
def getInvoice(request):
    invoice = Invoice.objects.get(invoiceId=2)

    serializers = InvoiceSerializer(invoice,many =False)
    return Response(serializers.data)
