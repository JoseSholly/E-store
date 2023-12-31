# Generated by Django 4.1 on 2023-10-08 14:43

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[900, 900], upload_to='Resized_media/%Y/%m/%d'),
        ),
    ]
