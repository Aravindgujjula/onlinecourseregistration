# Generated by Django 3.0.7 on 2020-07-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='Duration',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
