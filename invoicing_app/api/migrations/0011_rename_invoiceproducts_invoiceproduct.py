# Generated by Django 3.2.5 on 2021-08-19 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210818_1018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceProducts',
            new_name='InvoiceProduct',
        ),
    ]
