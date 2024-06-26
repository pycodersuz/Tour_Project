# Generated by Django 5.0.6 on 2024-05-21 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_agency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='aircategory',
        ),
        migrations.AddField(
            model_name='aircategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aircategory', to='tour_agency.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircategory',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
