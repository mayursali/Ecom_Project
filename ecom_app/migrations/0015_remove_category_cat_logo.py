# Generated by Django 4.2.4 on 2023-08-17 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0014_remove_main_category_description_main_category_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_logo',
        ),
    ]