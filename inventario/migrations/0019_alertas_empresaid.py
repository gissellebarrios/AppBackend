# Generated by Django 5.0.7 on 2024-12-20 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0018_movimiento_empresaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertas',
            name='empresaid',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='inventario.empresa'),
        ),
    ]
