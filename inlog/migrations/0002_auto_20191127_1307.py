# Generated by Django 2.2.7 on 2019-11-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='host',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.TextField(max_length=30),
        ),
    ]
