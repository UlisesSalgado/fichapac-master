# Generated by Django 5.1.1 on 2024-10-26 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichapac', '0004_paciente_domicilio_paciente_edad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='user',
        ),
    ]
