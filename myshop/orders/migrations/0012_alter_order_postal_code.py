# Generated by Django 4.1 on 2023-11-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_order_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
