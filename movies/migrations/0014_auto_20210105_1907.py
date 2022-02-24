# Generated by Django 3.1.1 on 2021-01-05 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20210105_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='cinema',
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='movies.seat'),
            preserve_default=False,
        ),
    ]
