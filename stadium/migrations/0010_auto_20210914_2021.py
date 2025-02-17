# Generated by Django 3.1.6 on 2021-09-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0009_auto_20210912_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='golden_seats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='golden_seats_price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='medium_seats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='medium_seats_price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='no_player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='platinum_seats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='platinum_seats_price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='silver_seats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='silver_seats_price',
        ),
        migrations.AddField(
            model_name='game',
            name='game_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='game_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='last_booking',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='stadium_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_choices',
            field=models.IntegerField(blank=True, choices=[(1, 'VIP'), (2, 'Local')], null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stadium.gamecategory'),
        ),
    ]
