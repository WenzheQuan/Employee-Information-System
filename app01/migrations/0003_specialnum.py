# Generated by Django 4.0.6 on 2022-07-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_depart_alter_userinfo_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(verbose_name='Mobile')),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('level', models.SmallIntegerField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')], verbose_name='Level')),
                ('Status', models.SmallIntegerField(choices=[(1, 'Available'), (2, 'Occupied')], verbose_name='Status')),
            ],
        ),
    ]
