# Generated by Django 5.0 on 2024-01-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('count', models.IntegerField(verbose_name='人口')),
                ('img', models.FileField(max_length=128, upload_to='city/', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='XX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('image', models.FileField(upload_to='avatar/', verbose_name='头像')),
            ],
        ),
    ]
