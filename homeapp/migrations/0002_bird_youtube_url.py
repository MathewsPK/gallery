# Generated by Django 5.2.4 on 2025-07-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
