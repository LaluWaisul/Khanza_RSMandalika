# Generated by Django 4.1 on 2023-03-12 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_bangsal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bangsal',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bidang',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='departement',
            options={
                'db_table': 'departement',
                'managed': False
                },
        ),
    ]
