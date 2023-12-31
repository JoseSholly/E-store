# Generated by Django 4.1 on 2023-11-19 15:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_alter_coupon_discount'),
        ('orders', '0005_alter_order_first_name_alter_order_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_coupon', to='coupons.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
