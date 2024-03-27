# Generated by Django 4.2.4 on 2024-03-27 09:11

import django.contrib.postgres.fields
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0226_rename_typ_e_celllinedoc_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalcellline',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalinhibitor',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicaloligo',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicaloligo',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalplasmid',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalplasmid',
            name='history_formz_ecoli_strains',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='e. coli strains'),
        ),
        migrations.AlterField(
            model_name='historicalplasmid',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalplasmid',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalplasmid',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_all_plasmids_in_stocked_strain',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='all plasmids in stocked strain'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_cassette_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='cassette plasmids'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalsacerevisiaestrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_all_plasmids_in_stocked_strain',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='all plasmids in stocked strain'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_cassette_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='cassette plasmids'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalscpombestrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='historicalsirna',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalsirna',
            name='history_orders',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='historicalsirna',
            name='locus_ids',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='historicalsirna',
            name='target_genes',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=15), default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_genotyping_oligos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genotyping oligos'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_integrated_oligos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated oligos'),
        ),
        migrations.AlterField(
            model_name='historicalwormstrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmids'),
        ),
        migrations.AlterField(
            model_name='inhibitor',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='oligo',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='oligo',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='history_formz_ecoli_strains',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='e. coli strains'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_all_plasmids_in_stocked_strain',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='all plasmids in stocked strain'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_cassette_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='cassette plasmids'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='sacerevisiaestrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_all_plasmids_in_stocked_strain',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='all plasmids in stocked strain'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_cassette_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='cassette plasmids'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_episomal_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='episomal plasmids'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='scpombestrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmid'),
        ),
        migrations.AlterField(
            model_name='sirna',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='sirna',
            name='history_orders',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='sirna',
            name='locus_ids',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='sirna',
            name='target_genes',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=15), default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_documents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_formz_elements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formz elements'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_formz_gentech_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genTech methods'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_formz_projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='formZ projects'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_genotyping_oligos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='genotyping oligos'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_integrated_oligos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated oligos'),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='history_integrated_plasmids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, null=True, size=None, verbose_name='integrated plasmids'),
        ),
    ]
