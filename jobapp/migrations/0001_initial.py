# Generated by Django 4.2.6 on 2023-11-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memail', models.EmailField(max_length=254)),
                ('mpassword', models.CharField(max_length=20)),
            ],
        ),
    ]