# Generated by Django 3.1.7 on 2021-05-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20210516_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeebar',
            name='image',
            field=models.ImageField(null=True, upload_to='menus'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='coffee_bars'),
        ),
    ]
