# Generated by Django 4.2.4 on 2024-03-25 14:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0225_alter_oligo_sequence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='celllinedoc',
            old_name='typ_e',
            new_name='description',
        ),
        migrations.AddField(
            model_name='antibody',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='ecolistrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalantibody',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalecolistrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalinhibitor',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicaloligo',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalplasmid',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalsacerevisiaestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalscpombestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalsirna',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='historicalwormstrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='inhibitor',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='oligo',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='plasmid',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='sacerevisiaestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='scpombestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='sirna',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='wormstrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='celllinedoc',
            name='last_changed_date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='last changed'),
        ),
        migrations.AlterField(
            model_name='celllinedoc',
            name='name',
            field=models.FileField(null=True, upload_to='temp/', verbose_name='file name'),
        ),
        migrations.CreateModel(
            name='WormStrainDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('worm_strain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.wormstrain')),
            ],
            options={
                'verbose_name': 'worm strain document',
            },
        ),
        migrations.CreateModel(
            name='SiRnaDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('si_rna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.sirna')),
            ],
            options={
                'verbose_name': 'siRNA document',
            },
        ),
        migrations.CreateModel(
            name='ScPombeStrainDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('scpombe_strain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.scpombestrain')),
            ],
            options={
                'verbose_name': 'sc. pombe strain document',
            },
        ),
        migrations.CreateModel(
            name='SaCerevisiaeStrainDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('sacerevisiae_strain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.sacerevisiaestrain')),
            ],
            options={
                'verbose_name': 'sa. cerevisiae strain document',
            },
        ),
        migrations.CreateModel(
            name='PlasmidDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('plasmid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.plasmid')),
            ],
            options={
                'verbose_name': 'plasmid document',
            },
        ),
        migrations.CreateModel(
            name='OligoDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('oligo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.oligo')),
            ],
            options={
                'verbose_name': 'oligo document',
            },
        ),
        migrations.CreateModel(
            name='InhibitorDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('inhibitor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.inhibitor')),
            ],
            options={
                'verbose_name': 'inhibitor document',
            },
        ),
        migrations.CreateModel(
            name='EColiStrainDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('ecoli_strain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.ecolistrain')),
            ],
            options={
                'verbose_name': 'e. coli strain document',
            },
        ),
        migrations.CreateModel(
            name='AntibodyDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='temp/', verbose_name='file name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='comment')),
                ('created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_changed_date_time', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('antibody', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.antibody')),
            ],
            options={
                'verbose_name': 'antibody document',
            },
        ),
    ]
