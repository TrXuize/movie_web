# Generated by Django 3.1.1 on 2021-01-05 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20210105_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='cinema',
        ),
        migrations.AddField(
            model_name='seat',
            name='session',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='movies.cinema_session'),
            preserve_default=False,
        ),
    ]
