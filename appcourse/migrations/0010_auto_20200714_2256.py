# Generated by Django 3.0.7 on 2020-07-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcourse', '0009_auto_20200711_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centermodel',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]