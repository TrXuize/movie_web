# Generated by Django 3.1.1 on 2020-12-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20201223_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(max_length=20),
        ),
    ]
