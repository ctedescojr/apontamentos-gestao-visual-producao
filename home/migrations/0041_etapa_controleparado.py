# Generated by Django 4.1.4 on 2023-06-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_etapa_faltamaterial_etapa_necessidadespessoais_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapa',
            name='controleParado',
            field=models.IntegerField(default=0),
        ),
    ]
