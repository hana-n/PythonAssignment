# Generated by Django 2.1.7 on 2019-03-09 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0005_auto_20190309_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
