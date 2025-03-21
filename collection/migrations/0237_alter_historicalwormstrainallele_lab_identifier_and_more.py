# Generated by Django 4.2.4 on 2024-12-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0236_alter_historicalwormstrain_location_backup_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalwormstrainallele",
            name="lab_identifier",
            field=models.CharField(max_length=15, verbose_name="prefix/Lab identifier"),
        ),
        migrations.AlterField(
            model_name="historicalwormstrainallele",
            name="mutation",
            field=models.CharField(
                blank=True,
                help_text="Genotype",
                max_length=255,
                verbose_name="mutation",
            ),
        ),
        migrations.AlterField(
            model_name="historicalwormstrainallele",
            name="transgene",
            field=models.CharField(
                blank=True,
                help_text="Genotype",
                max_length=255,
                verbose_name="transgene",
            ),
        ),
        migrations.AlterField(
            model_name="wormstrainallele",
            name="lab_identifier",
            field=models.CharField(max_length=15, verbose_name="prefix/Lab identifier"),
        ),
        migrations.AlterField(
            model_name="wormstrainallele",
            name="mutation",
            field=models.CharField(
                blank=True,
                help_text="Genotype",
                max_length=255,
                verbose_name="mutation",
            ),
        ),
        migrations.AlterField(
            model_name="wormstrainallele",
            name="transgene",
            field=models.CharField(
                blank=True,
                help_text="Genotype",
                max_length=255,
                verbose_name="transgene",
            ),
        ),
    ]
