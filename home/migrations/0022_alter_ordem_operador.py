# Generated by Django 3.2.8 on 2021-10-17 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_etapa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='operador',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='home.funcionario'),
        ),
    ]