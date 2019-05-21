# Generated by Django 2.1.8 on 2019-05-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0105_auto_20190521_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacerevisiaestrainepisomalplasmid',
            name='created_date',
            field=models.DateField(blank=True, null=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrainepisomalplasmid',
            name='formz_project',
            field=models.ManyToManyField(blank=True, related_name='cerevisiae_episomal_plasmids_projects', to='formz.FormZProject'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrainepisomalplasmid',
            name='present_in_stocked_strain',
            field=models.BooleanField(default=False, null=True, verbose_name='present in -80° C stock?'),
        ),
    ]
