# Generated by Django 5.0.3 on 2024-03-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(db_index=True, max_length=255)),
                ('city_name', models.CharField(db_index=True, max_length=100)),
                ('date', models.DateField(db_index=True)),
                ('time', models.TimeField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'indexes': [models.Index(fields=['city_name', 'date'], name='event_api_e_city_na_8db576_idx'), models.Index(fields=['latitude', 'longitude'], name='event_api_e_latitud_906fbd_idx')],
            },
        ),
    ]