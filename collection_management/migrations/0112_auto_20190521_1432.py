# Generated by Django 2.1.8 on 2019-05-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0111_auto_20190521_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='a_pplication',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='application'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='catalogue_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='catalogue number'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='clone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='clone'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='description_comment',
            field=models.TextField(blank=True, null=True, verbose_name='description/comments'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='info_sheet',
            field=models.FileField(blank=True, null=True, upload_to='collection_management/antibody/', verbose_name='info sheet (max. 2 MB)'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='l_ocation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='received_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='receieved from'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='species_isotype',
            field=models.CharField(max_length=255, null=True, verbose_name='species/isotype'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='genotype',
            field=models.TextField(blank=True, null=True, verbose_name='genotype'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='note'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='purpose',
            field=models.TextField(blank=True, null=True, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='resistance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='resistance'),
        ),
        migrations.AlterField(
            model_name='ecolistrain',
            name='us_e',
            field=models.CharField(choices=[('Cloning', 'Cloning'), ('Expression', 'Expression'), ('Other', 'Other')], max_length=255, null=True, verbose_name='use'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='a_pplication',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='application'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='catalogue_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='catalogue number'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='clone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='clone'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='description_comment',
            field=models.TextField(blank=True, null=True, verbose_name='description/comments'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='info_sheet',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='info sheet (max. 2 MB)'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='l_ocation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='received_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='receieved from'),
        ),
        migrations.AlterField(
            model_name='historicalantibody',
            name='species_isotype',
            field=models.CharField(max_length=255, null=True, verbose_name='species/isotype'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='genotype',
            field=models.TextField(blank=True, null=True, verbose_name='genotype'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='note'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='purpose',
            field=models.TextField(blank=True, null=True, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='resistance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='resistance'),
        ),
        migrations.AlterField(
            model_name='historicalecolistrain',
            name='us_e',
            field=models.CharField(choices=[('Cloning', 'Cloning'), ('Expression', 'Expression'), ('Other', 'Other')], max_length=255, null=True, verbose_name='use'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='alternative_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='alternative name'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='box_name',
            field=models.CharField(max_length=255, null=True, verbose_name='box'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='cell_type_tissue',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cell type/tissue'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='culture_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='culture type'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='description_comment',
            field=models.TextField(blank=True, null=True, verbose_name='description/comments'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='freezing_medium',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='freezing medium'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='growth_condition',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='growth conditions'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='name',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='organism',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='organism'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='parental_line_old',
            field=models.CharField(max_length=255, null=True, verbose_name='parental cell line'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='received_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='received from'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='alternative_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='alternative name'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='box_name',
            field=models.CharField(max_length=255, null=True, verbose_name='box'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='cell_type_tissue',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cell type/tissue'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='culture_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='culture type'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='description_comment',
            field=models.TextField(blank=True, null=True, verbose_name='description/comments'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='freezing_medium',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='freezing medium'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='growth_condition',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='growth conditions'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='organism',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='organism'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='parental_line_old',
            field=models.CharField(max_length=255, null=True, verbose_name='parental cell line'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='received_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='received from'),
        ),
        migrations.AlterField(
            model_name='mammalianlinedoc',
            name='comment',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='mammalianlinedoc',
            name='date_of_test',
            field=models.DateField(null=True, verbose_name='date of test'),
        ),
        migrations.AlterField(
            model_name='mammalianlinedoc',
            name='name',
            field=models.FileField(null=True, upload_to='temp/', verbose_name='file name'),
        ),
        migrations.AlterField(
            model_name='mammalianlinedoc',
            name='typ_e',
            field=models.CharField(choices=[['virus', 'Virus test'], ['mycoplasma', 'Mycoplasma test'], ['fingerprint', 'Fingerprinting'], ['other', 'Other']], max_length=255, null=True, verbose_name='doc type'),
        ),
    ]
