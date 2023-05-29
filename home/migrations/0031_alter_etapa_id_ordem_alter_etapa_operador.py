# Generated by Django 4.1.2 on 2022-11-26 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_funcionario_options_alter_modelo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='id_ordem',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='home.ordem'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='operador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.funcionario'),
        ),
    ]
