# Generated by Django 3.2.11 on 2022-01-27 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tinyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='shortUrl',
            new_name='short_url',
        ),
        migrations.RemoveField(
            model_name='url',
            name='longUrl',
        ),
        migrations.AddField(
            model_name='url',
            name='long_url',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
