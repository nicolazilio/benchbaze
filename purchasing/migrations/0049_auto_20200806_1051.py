# Generated by Django 2.2.13 on 2020-08-06 08:51

from django.db import migrations, models

import purchasing.models


class Migration(migrations.Migration):
    dependencies = [
        ("purchasing", "0048_auto_20191106_1616"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalorder",
            name="cas_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="CAS number",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="ghs_pictogram",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="GHS pictogram",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="part_description",
            field=models.CharField(
                help_text="To see suggestions, type three characters or more",
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="part description",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="price",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="price",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="quantity",
            field=models.CharField(
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="quantity",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="supplier",
            field=models.CharField(
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="supplier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="supplier_part_no",
            field=models.CharField(
                help_text="To see suggestions, type three characters or more",
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="supplier Part-No",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="cas_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="CAS number",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="ghs_pictogram",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="GHS pictogram",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="part_description",
            field=models.CharField(
                help_text="To see suggestions, type three characters or more",
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="part description",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="price",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.CharField(
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="quantity",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="supplier",
            field=models.CharField(
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="supplier",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="supplier_part_no",
            field=models.CharField(
                help_text="To see suggestions, type three characters or more",
                max_length=255,
                validators=[purchasing.models.validate_absence_airquotes],
                verbose_name="supplier Part-No",
            ),
        ),
    ]
