# Generated by Django 3.1.1 on 2020-12-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201224_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='total_time',
            field=models.CharField(max_length=10),
        ),
    ]