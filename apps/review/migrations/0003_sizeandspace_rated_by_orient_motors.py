# Generated by Django 4.2.2 on 2023-09-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_safetyandconvenience_safetyandconvenienceadvantages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizeandspace',
            name='rated_by_orient_motors',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
