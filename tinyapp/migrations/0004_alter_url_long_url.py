# Generated by Django 3.2.11 on 2022-01-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyapp', '0003_auto_20220128_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(),
        ),
    ]
