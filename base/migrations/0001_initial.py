# Generated by Django 5.0.1 on 2024-01-30 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=255)),
                ('sub_county', models.CharField(max_length=255)),
                ('ward', models.CharField(max_length=255)),
                ('building_name', models.CharField(blank=True, max_length=255)),
                ('floor', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('age', models.PositiveIntegerField(editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.business_category')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.location')),
            ],
        ),
    ]
