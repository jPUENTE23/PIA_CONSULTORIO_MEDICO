# Generated by Django 4.0.3 on 2022-05-11 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pagos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagos',
            old_name='IdCita',
            new_name='NoCita',
        ),
    ]
