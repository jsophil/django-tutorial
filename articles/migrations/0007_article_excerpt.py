# Generated by Django 2.1.4 on 2018-12-15 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20181214_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
