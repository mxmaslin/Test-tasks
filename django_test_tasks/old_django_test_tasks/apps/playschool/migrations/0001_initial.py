# Generated by Django 2.1.1 on 2020-07-31 12:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('has_came_with', models.CharField(choices=[('M', 'Mother'), ('F', 'Father')], default='M', max_length=1)),
                ('time_arrived', models.DateTimeField()),
                ('time_departed', models.DateTimeField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='playschool/images/%Y/%m/%d')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Boy'), ('F', 'Girl')], default='F', max_length=1)),
                ('birth_date', models.DateField()),
                ('school_class', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('is_studying', models.BooleanField()),
            ],
            options={
                'ordering': ('school_class', 'name'),
            },
        ),
        migrations.AddField(
            model_name='record',
            name='scholar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playschool.Scholar'),
        ),
    ]
