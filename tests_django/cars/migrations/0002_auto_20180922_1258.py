# Generated by Django 2.0.7 on 2018-09-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='uid',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='uid',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
