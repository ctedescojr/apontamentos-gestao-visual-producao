# Generated by Django 3.2.8 on 2021-10-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211008_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etapa',
            old_name='concerto',
            new_name='conserto',
        ),
    ]