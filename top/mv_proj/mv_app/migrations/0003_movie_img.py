# Generated by Django 4.1.5 on 2023-01-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mv_app', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='qwerty', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
