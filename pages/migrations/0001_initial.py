# Generated by Django 3.2.7 on 2021-10-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestBuy',
            fields=[
                ('BestBuy_Name', models.CharField(max_length=256)),
                ('BestBuy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BeestBuy_Status', models.CharField(max_length=32)),
                ('BestBuy_Ratings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('BestBuy_Review', models.IntegerField()),
                ('BestBuy_ModelNumber', models.CharField(max_length=128)),
                ('BestBuy_SKU', models.IntegerField(primary_key=True, serialize=False)),
                ('BestBuy_URL', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('product', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('MicroCenter_SKU', models.IntegerField()),
                ('BestBuy_SKU', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]
