# Generated by Django 3.2.14 on 2022-07-21 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_labuser_identifier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labuser',
            old_name='identifier',
            new_name='oidc_identifier',
        ),
    ]
