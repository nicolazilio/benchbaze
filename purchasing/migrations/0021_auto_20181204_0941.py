# Generated by Django 1.11 on 2018-12-04 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchasing", "0020_auto_20181128_1604"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="purchasing.Location",
            ),
        ),
    ]
