# Generated by Django 4.2.4 on 2023-08-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_category_rename_brand_banner_discount_offer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Category_Description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
