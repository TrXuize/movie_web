# Generated by Django 3.1.1 on 2021-01-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_auto_20210106_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat',
            field=models.IntegerField(default=''),
        ),
    ]