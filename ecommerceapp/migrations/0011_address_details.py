# Generated by Django 5.0.4 on 2024-05-03 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0010_remove_wishlist_size_chart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField()),
                ('userdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.userregister')),
            ],
        ),
    ]
