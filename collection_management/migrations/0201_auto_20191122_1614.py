# Generated by Django 2.1.13 on 2019-11-22 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0078_auto_20191117_1549'),
        ('collection_management', '0200_auto_20191122_1611'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MammalianLineEpisomalPlasmid',
            new_name='CellLineEpisomalPlasmid',
        ),
    ]
