# Generated by Django 4.0.6 on 2022-07-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_specialnum_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialnum',
            old_name='Price',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='specialnum',
            name='level',
            field=models.SmallIntegerField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')], default=1, verbose_name='Level'),
        ),
    ]
