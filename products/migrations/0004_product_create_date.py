# Generated by Django 4.2.4 on 2023-08-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_description_product_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
