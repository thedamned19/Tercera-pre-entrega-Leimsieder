# Generated by Django 4.1.5 on 2023-01-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaApp', '0002_autor_lector_libro_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='multa',
            field=models.BooleanField(default=False),
        ),
    ]