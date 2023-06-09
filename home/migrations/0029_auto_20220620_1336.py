# Generated by Django 3.2.8 on 2022-06-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_etapa_colmeia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='modelo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='cliente',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='tipo',
            field=models.CharField(choices=[('N', 'Nova'), ('R', 'Retrabalho'), ('G', 'Garantia'), ('2', 'Outro')], max_length=1),
        ),
    ]
