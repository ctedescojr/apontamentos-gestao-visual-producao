# Generated by Django 3.2.8 on 2021-10-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211011_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='fim',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='inicio',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
