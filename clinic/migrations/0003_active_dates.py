# Generated by Django 4.1.1 on 2022-10-01 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_doctor_image_alter_clinic_address_alter_clinic_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='active_dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='active_date', to='clinic.doctor')),
            ],
        ),
    ]
