# Generated by Django 3.2.8 on 2021-10-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempo',
            name='etapa',
            field=models.CharField(choices=[('1', 'Etapa Um'), ('2', 'Etapa Dois'), ('3', 'Etapa Três')], max_length=1),
        ),
    ]