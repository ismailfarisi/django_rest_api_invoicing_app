from re import M
from django.db import models
from django.db.models import fields
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
    product = ProductSerializer(many = False)
    class Meta:
        model =InvoiceProduct
        fields = ["product",'quantity','unitRate']

class InvoiceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    invoice_products = InvoiceProductSerializer(many=True)
    class Meta:
        model =Invoice
        fields = ["invoiceId","company","date","invoice_products"]

