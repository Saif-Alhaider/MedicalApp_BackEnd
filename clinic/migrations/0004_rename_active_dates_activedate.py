# Generated by Django 4.1.1 on 2022-10-01 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_active_dates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='active_dates',
            new_name='ActiveDate',
        ),
    ]
