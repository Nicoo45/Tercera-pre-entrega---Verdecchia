# Generated by Django 4.1.6 on 2023-03-03 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allclubs', '0002_remove_clubs_numero_club_alter_clubs_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deportistas',
            old_name='fecha_ingreso',
            new_name='fechaingreso',
        ),
    ]
