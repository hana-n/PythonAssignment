# Generated by Django 2.1.7 on 2019-03-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0024_auto_20190316_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='review-images'),
        ),
    ]
