# Generated by Django 5.1.2 on 2024-11-03 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('gender', models.CharField(choices=[('M', 'MaLe'), ('F', 'Female')], default='M', max_length=20)),
                ('races_count', models.IntegerField()),
                ('inserted_timespan', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('manufacturing_date', models.DateTimeField()),
                ('has_it_competed', models.BooleanField(default=False)),
                ('inserted_timespan', models.DateTimeField(auto_now_add=True)),
                ('drone_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drones', to='drone.dronecategory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_feet', models.IntegerField()),
                ('distance_achievement_date', models.DateTimeField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.drone')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='drone.pilot')),
            ],
            options={
                'ordering': ['-distance_in_feet'],
            },
        ),
    ]