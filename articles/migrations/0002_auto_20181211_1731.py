# Generated by Django 2.1.4 on 2018-12-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
