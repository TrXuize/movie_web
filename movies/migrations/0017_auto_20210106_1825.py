# Generated by Django 3.1.1 on 2021-01-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20210105_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat',
            field=models.IntegerField(),
        ),
    ]