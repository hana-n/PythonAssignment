# Generated by Django 2.1.7 on 2019-03-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0028_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(default='', null=True, upload_to='review-photos'),
        ),
    ]
