# Generated by Django 3.2.6 on 2021-09-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0004_auto_20210909_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created',
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='created',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
