# Generated by Django 5.0.6 on 2024-06-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pokedex_number', models.IntegerField()),
                ('primary_type', models.CharField(max_length=15)),
                ('secondary_type', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
