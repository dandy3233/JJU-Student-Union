# Generated by Django 5.1.3 on 2024-12-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_imagecollage_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollage',
            name='tiktok',
            field=models.URLField(blank=True, null=True),
        ),
    ]
