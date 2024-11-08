# Generated by Django 5.1.1 on 2024-10-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapac', '0003_historiaclinica_descripcion_historiaclinica_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='domicilio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numafiliado',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
