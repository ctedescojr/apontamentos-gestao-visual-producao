# Generated by Django 4.1.4 on 2023-08-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_ordem_tem_acessorio_alter_etapa_controleparado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='tem_acessorio',
            field=models.BooleanField(default=False, verbose_name='Tem acessório?'),
        ),
    ]
