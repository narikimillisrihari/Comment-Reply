# Generated by Django 3.2.24 on 2024-02-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_post',
            name='add_comment',
            field=models.CharField(max_length=255),
        ),
    ]