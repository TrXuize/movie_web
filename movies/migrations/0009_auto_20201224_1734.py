# Generated by Django 3.1.1 on 2020-12-24 09:34

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20201224_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to=movies.models.get_image_path),
        ),
    ]
