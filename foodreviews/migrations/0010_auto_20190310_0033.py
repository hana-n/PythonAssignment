# Generated by Django 2.1.7 on 2019-03-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0009_auto_20190310_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Review Date'),
        ),
    ]
