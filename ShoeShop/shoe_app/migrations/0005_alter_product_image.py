# Generated by Django 4.2.5 on 2023-09-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe_app', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]