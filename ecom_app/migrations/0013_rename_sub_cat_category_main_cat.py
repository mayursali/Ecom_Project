# Generated by Django 4.2.4 on 2023-08-17 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0012_main_category_delete_main_caegory_category_sub_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Sub_cat',
            new_name='Main_cat',
        ),
    ]
