# Generated by Django 4.1.2 on 2022-10-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_hotelrank_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomcategory',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
