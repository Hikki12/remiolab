# Generated by Django 3.2.13 on 2022-06-12 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='css',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='dependencies',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='utils',
            field=models.TextField(blank=True),
        ),
    ]
