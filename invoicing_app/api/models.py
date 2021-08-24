from django.db import models



class Company(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    companyName = models.CharField(max_length=100,null=True)
    companyAdd1 = models.CharField(max_length=100,null=True)
    companyAdd2 = models.CharField(max_length=100,null=True)
    gstIn = models.CharField(max_length=100,null=True)

class Invoice(models.Model):
    invoiceId = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,null=True)
    date = models.DateField(null=True)

class Product(models.Model):
    productId = models.IntegerField(primary_key=True,auto_created=True)
    productName = models.CharField(max_length=100,null=True)
    hsnCode = models.IntegerField(null=True)
    defaultPrice = models.FloatField(null=True)

class InvoiceProduct(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True,related_name="invoice_products")
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True)
    quantity = models.FloatField(null=True)
    unitRate = models.FloatField(null=True)


