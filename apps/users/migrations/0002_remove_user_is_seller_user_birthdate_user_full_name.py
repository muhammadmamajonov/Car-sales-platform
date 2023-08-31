# Generated by Django 4.2.2 on 2023-08-11 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_seller',
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
