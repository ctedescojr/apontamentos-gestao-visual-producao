# Generated by Django 3.2.8 on 2021-10-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_ordem_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='obs',
            field=models.CharField(default='', max_length=200),
        ),
    ]
