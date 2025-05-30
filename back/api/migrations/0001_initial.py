# Generated by Django 5.1.7 on 2025-05-20 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig', models.IntegerField()),
                ('descricao', models.CharField(max_length=256)),
                ('ni', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sensores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(choices=[('temperatura', 'Temperatura (°C)'), ('umidade', 'Umidade (%)'), ('luminosidade', 'Luminosidade (lux)'), ('contador', 'Contador (num)')], max_length=20)),
                ('mac_adress', models.CharField(max_length=256)),
                ('unidade_med', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valor', models.FloatField()),
                ('timestamp', models.IntegerField()),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ambientes')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sensores')),
            ],
        ),
    ]
