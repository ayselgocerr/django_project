# Generated by Django 5.0 on 2023-12-17 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='departman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Personel', to='myproject.departman'),
        ),
    ]
