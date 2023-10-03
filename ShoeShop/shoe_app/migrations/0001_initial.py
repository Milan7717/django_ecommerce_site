# Generated by Django 4.2.5 on 2023-10-03 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(default='ShopName', max_length=200)),
                ('contact', models.CharField(default='', max_length=200)),
                ('brand', models.CharField(default='Brand name', max_length=200)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
                ('size', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('catogory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoe_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoe_app.people')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoe_app.product')),
            ],
        ),
    ]
