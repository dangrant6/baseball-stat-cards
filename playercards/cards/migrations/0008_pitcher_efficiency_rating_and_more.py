# Generated by Django 4.2.5 on 2024-01-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0007_remove_pitcher_efficiency_rating_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pitcher",
            name="efficiency_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="efficiency_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="net_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="net_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="performance_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="performance_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="predicted_war",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="war_last_year",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="pitcher",
            name="war_year_before_last",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="defense_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="defense_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="net_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="net_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="offense_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="offense_rating_percentile",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="predicted_war",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="war_last_year",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="positionplayer",
            name="war_year_before_last",
            field=models.FloatField(default=0),
        ),
    ]
