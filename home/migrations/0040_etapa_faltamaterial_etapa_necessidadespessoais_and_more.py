# Generated by Django 4.1.4 on 2023-06-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_etapa_almoco_etapa_fim_de_turno_etapa_outros_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapa',
            name='faltaMaterial',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='etapa',
            name='necessidadesPessoais',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='etapa',
            name='quebraFerramenta',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='almoco',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='fim_de_turno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='outros',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='setup',
            field=models.IntegerField(default=0),
        ),
    ]
