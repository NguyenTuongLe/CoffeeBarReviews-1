# Generated by Django 3.1.7 on 2021-05-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210516_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeebar',
            name='avg_vote',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
