# Generated by Django 5.0.7 on 2024-08-09 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_profile_clave_alter_profile_tipo_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='clave',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
