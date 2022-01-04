# Generated by Django 2.2 on 2020-06-22 14:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200622_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique_with=('customer__username', 'id')),
        ),
    ]