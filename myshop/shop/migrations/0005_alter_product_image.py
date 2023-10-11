# Generated by Django 4.1 on 2023-10-08 15:14

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_photo_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 500], upload_to='products/%Y/%m/%d'),
        ),
    ]