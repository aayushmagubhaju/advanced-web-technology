# Generated by Django 4.2.3 on 2023-07-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='file',
            name='picture',
        ),
        migrations.AddField(
            model_name='file',
            name='files',
            field=models.ImageField(blank=True, upload_to='Pictures'),
        ),
    ]
