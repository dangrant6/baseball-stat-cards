from django.core.management.base import BaseCommand, CommandError
from ...models import PositionPlayer, Pitcher
import numpy as np
import joblib
from decimal import Decimal

class Command(BaseCommand):
    def handle(self, *args, **options):
        model_position_players = joblib.load('cards/data/war_prediction_model_hitters_rf.pkl')
        model_pitchers = joblib.load('cards/data/war_prediction_model_hitters_rf.pkl')
        # Generate synthetic war data for the previous 2 years for hitters
        # Process Position Players
        for player in PositionPlayer.objects.all():
            # Generate synthetic war data
            player.war_last_year = player.war + Decimal(np.random.uniform(-1.5, 1.5))
            player.war_year_before_last = player.war_last_year + Decimal(np.random.uniform(-1.5, 1.5))
            player.save()

            # Predict future war using the model
            predicted_war = model_position_players.predict([[player.war_last_year, player.war_year_before_last]])
            player.predicted_war = predicted_war[0]
            player.save()

        # Process Pitchers
        for pitcher in Pitcher.objects.all():
            # Generate synthetic war data
            pitcher.war_last_year = pitcher.war + Decimal(np.random.uniform(-1.5, 1.5))
            pitcher.war_year_before_last = pitcher.war_last_year + Decimal(np.random.uniform(-1.5, 1.5))
            pitcher.save()

            # Predict future war using the model
            predicted_war = model_pitchers.predict([[pitcher.war_last_year, pitcher.war_year_before_last]])
            pitcher.predicted_war = predicted_war[0]
            pitcher.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated war predictions for players and pitchers'))