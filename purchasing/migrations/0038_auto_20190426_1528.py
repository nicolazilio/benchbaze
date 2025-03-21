# Generated by Django 2.1.8 on 2019-04-26 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchasing", "0037_auto_20190424_1236"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalorder",
            name="cost_unit",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="purchasing.CostUnit",
            ),
        ),
    ]
