# Generated by Django 3.2.8 on 2021-10-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211008_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='fase',
            field=models.CharField(choices=[('1', 'Fase2'), ('2', 'Fase2'), ('3', 'Fase3')], max_length=1),
        ),
    ]
