# Generated by Django 3.2.5 on 2021-08-17 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceproducts',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoiceproducts',
            name='product',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='InvoiceProducts',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]