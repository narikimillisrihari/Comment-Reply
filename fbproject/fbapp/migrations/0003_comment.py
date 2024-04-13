# Generated by Django 3.2.24 on 2024-02-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0002_alter_add_post_add_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('addpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fbapp.add_post')),
            ],
        ),
    ]
