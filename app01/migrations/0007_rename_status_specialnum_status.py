# Generated by Django 4.0.6 on 2022-07-15 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_rename_price_specialnum_price_alter_specialnum_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialnum',
            old_name='Status',
            new_name='status',
        ),
    ]
