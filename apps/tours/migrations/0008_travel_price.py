# Generated by Django 4.1.2 on 2022-10-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_travel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='price',
            field=models.IntegerField(default=300),
        ),
    ]
