# Generated by Django 4.2.4 on 2023-11-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_app', '0008_alter_reservas_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='cantidadClientes',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fechaReserva',
            field=models.DateField(),
        ),
    ]