# Generated by Django 2.1.8 on 2019-07-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0011_auto_20190716_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='formzbaseelement',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]
