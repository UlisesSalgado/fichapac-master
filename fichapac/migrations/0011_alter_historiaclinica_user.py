# Generated by Django 5.1.1 on 2024-10-26 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapac', '0010_alter_historiaclinica_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fichapac.paciente'),
        ),
    ]