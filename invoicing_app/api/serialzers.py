from rest_framework import serializers
from .models import Invoice, InvoiceProduct, Product ,Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId','productName','hsnCode']

class InvoiceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =InvoiceProduct
        fields = ["product",'quantity','unitRate']

    def to_representation(self, instance):
        self.fields['product'] = ProductSerializer(read_only = True)
        return super(InvoiceProductSerializer,self).to_representation(instance)

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_products = InvoiceProductSerializer(many=True)
    class Meta:
        model =Invoice
        fields = ["invoiceId","company","date","invoice_products"]

    def to_representation(self, instance):
        self.fields['company'] = CompanySerializer(read_only = True)
        return super(InvoiceSerializer,self).to_representation(instance)
    
    def create(self, validated_data):
        products_data = validated_data.pop('invoice_products')
        invoice = Invoice.objects.create(**validated_data)
        for product_data in products_data:
            InvoiceProduct.objects.create(user=invoice, **product_data)
        return invoice

