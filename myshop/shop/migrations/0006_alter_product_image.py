# Generated by Django 4.1 on 2023-10-08 15:18

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[200, 200], upload_to='products/%Y/%m/%d'),
        ),
    ]