from django.contrib import admin
from .models import Invoice,Company,Product,InvoiceProduct

admin.site.register([Invoice,Company,Product,InvoiceProduct])


