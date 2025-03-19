# Generated by Django 3.1.6 on 2021-05-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchasing", "0050_auto_20200806_1201"),
    ]

    operations = [
        migrations.CreateModel(
            name="GhsSymbol",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=10, unique=True, verbose_name="code"),
                ),
                (
                    "pictogram",
                    models.ImageField(
                        help_text="only .png images, max. 2 MB",
                        upload_to="temp/",
                        verbose_name="pictogram",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "GHS symbol",
            },
        ),
        migrations.CreateModel(
            name="SignalWord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "signal_words",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="signal word"
                    ),
                ),
            ],
            options={
                "verbose_name": "signal word",
            },
        ),
        migrations.RenameField(
            model_name="historicalorder",
            old_name="ghs_pictogram",
            new_name="ghs_pictogram_old",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="ghs_pictogram",
            new_name="ghs_pictogram_old",
        ),
        migrations.AddField(
            model_name="historicalorder",
            name="ghs_symbols_autocomplete",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="historicalorder",
            name="history_ghs_symbols",
            field=models.TextField(blank=True, verbose_name="GHS symbols"),
        ),
        migrations.AddField(
            model_name="historicalorder",
            name="history_signal_words",
            field=models.TextField(blank=True, verbose_name="signal words"),
        ),
        migrations.AddField(
            model_name="historicalorder",
            name="signal_words_autocomplete",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="order",
            name="ghs_symbols_autocomplete",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="order",
            name="history_ghs_symbols",
            field=models.TextField(blank=True, verbose_name="GHS symbols"),
        ),
        migrations.AddField(
            model_name="order",
            name="history_signal_words",
            field=models.TextField(blank=True, verbose_name="signal words"),
        ),
        migrations.AddField(
            model_name="order",
            name="signal_words_autocomplete",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="order",
            name="ghs_symbols",
            field=models.ManyToManyField(
                blank=True,
                related_name="order_ghs_symbols",
                to="purchasing.GhsSymbol",
                verbose_name="GHS symbols",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="signal_words",
            field=models.ManyToManyField(
                blank=True,
                related_name="order_signal_words",
                to="purchasing.SignalWord",
                verbose_name="signal words",
            ),
        ),
    ]
