# Generated by Django 5.0.1 on 2024-01-31 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_business_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name_plural': 'Businesses'},
        ),
    ]