# Generated by Django 3.2.5 on 2021-08-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210817_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyAdd1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyAdd2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='gstIn',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
