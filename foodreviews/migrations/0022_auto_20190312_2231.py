# Generated by Django 2.1.7 on 2019-03-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0021_auto_20190311_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='foodreviews.Restaurant'),
        ),
    ]
