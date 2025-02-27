# Generated by Django 3.2.13 on 2022-08-15 07:50

import django.contrib.postgres.indexes
from django.db import migrations, models
from django.contrib.postgres.operations import BtreeGinExtension, BtreeGistExtension, TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ('indexes_task_1', '0002_auto_20220808_1124'),
    ]

    operations = [
	BtreeGinExtension(),
        BtreeGistExtension(),
        TrigramExtension(),
        migrations.AlterField(
            model_name='employee',
            name='additional_info',
            field=models.TextField(db_index=True, default='', verbose_name='Дополнительная информация'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['fname', 'iname', 'oname'], name='indexes_emp_fname_1395cf_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=django.contrib.postgres.indexes.GinIndex(fields=['country'], name='indexes_emp_country_afefd7_gin'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=django.contrib.postgres.indexes.GistIndex(fields=['begin', 'end'], name='indexes_emp_begin_66e5cc_gist'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=django.contrib.postgres.indexes.GinIndex(fields=['additional_info'], name='additional_info_gin_index', opclasses=['gin_trgm_ops']),
        ),
    ]
