# Generated by Django 4.2.5 on 2024-01-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0003_pitcher_efficiency_rating_pitcher_net_rating_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pitcher",
            name="efficiency_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="net_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="performance_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="defense_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="net_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="offense_rating_percentile",
            field=models.FloatField(default=0),
        ),
    ]
