# Generated by Django 2.2.7 on 2019-11-28 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inlog', '0002_auto_20191127_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='inTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
