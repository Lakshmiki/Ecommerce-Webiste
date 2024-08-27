# Generated by Django 5.0.4 on 2024-04-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('propic', models.ImageField(upload_to='image/')),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
