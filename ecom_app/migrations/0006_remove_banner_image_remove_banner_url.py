# Generated by Django 4.2.4 on 2023-08-17 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0005_rename_featured_product_banner_featured_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='Url',
        ),
    ]