# Generated by Django 2.2.11 on 2022-06-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
