# Generated by Django 3.2.8 on 2021-10-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20211021_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapa',
            name='colmeia',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1),
        ),
    ]
