# Generated by Django 4.1 on 2023-11-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_favorites_favorites_shop_favori_user_id_25b91d_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='items',
            field=models.ManyToManyField(null=True, related_name='saved_items', to='shop.product'),
        ),
    ]
