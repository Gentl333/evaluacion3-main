# Generated by Django 4.1.2 on 2024-07-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionviajes', '0002_paqueteturistico_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paqueteturistico',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
