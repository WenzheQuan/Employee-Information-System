# Generated by Django 4.0.6 on 2022-07-15 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_rename_status_specialnum_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpecialNum',
            new_name='SuperNum',
        ),
    ]
