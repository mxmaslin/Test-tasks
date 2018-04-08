# Generated by Django 2.0.4 on 2018-04-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(null=True)),
                ('file', models.FileField(null=True, upload_to='uploads/')),
                ('format', models.CharField(choices=[('jpeg', 'jpg'), ('gif', 'gif'), ('png', 'png')], default='jpeg', max_length=3)),
                ('jpeg_quality', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('name', 'created'),
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_sizer.Image')),
            ],
        ),
    ]
