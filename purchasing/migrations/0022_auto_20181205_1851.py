# Generated by Django 1.11 on 2018-12-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchasing", "0021_auto_20181204_0941"),
    ]

    operations = [
        migrations.AlterField(
            model_name="msdsform",
            name="name",
            field=models.FileField(
                upload_to="purchasing/msdsform/", verbose_name="File name"
            ),
        ),
    ]
