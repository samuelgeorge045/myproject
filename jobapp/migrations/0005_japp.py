# Generated by Django 4.2.6 on 2023-12-07 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_jpostmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='japp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecom', models.CharField(max_length=20)),
                ('edsgn', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=20)),
                ('eemail', models.EmailField(max_length=254)),
                ('equal', models.CharField(max_length=20)),
                ('eph', models.IntegerField()),
                ('eexp', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='jobapp/static')),
            ],
        ),
    ]
