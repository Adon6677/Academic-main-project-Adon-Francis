# Generated by Django 3.1.6 on 2021-09-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0002_auto_20210909_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
