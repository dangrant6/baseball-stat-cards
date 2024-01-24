from django.core.management.base import BaseCommand
from ...models import Pitcher, PositionPlayer
from .calculations import (
    calculate_performance_rating, 
    calculate_efficiency_rating, 
    calculate_offense_rating, 
    calculate_defense_rating,
    calculate_net_rating_for_pitcher,
    calculate_net_rating_for_player
)
from django.db.models import F
from scipy.stats import percentileofscore

class Command(BaseCommand):
    help = 'Calculate player ratings and percentiles'

    def handle(self, *args, **options):
        # Calculate ratings for pitchers
        for pitcher in Pitcher.objects.all():
            pitcher.performance_rating = calculate_performance_rating(pitcher)
            pitcher.efficiency_rating = calculate_efficiency_rating(pitcher)
            pitcher.net_rating = calculate_net_rating_for_pitcher(pitcher)
            pitcher.save()

        # Calculate ratings for position players
        for player in PositionPlayer.objects.all():
            player.offense_rating = calculate_offense_rating(player)
            player.defense_rating = calculate_defense_rating(player)
            player.net_rating = calculate_net_rating_for_player(player)
            player.save()

        # Calculate percentiles
        self.calculate_percentiles(Pitcher, ['performance_rating', 'efficiency_rating', 'net_rating'])
        self.calculate_percentiles(PositionPlayer, ['offense_rating', 'defense_rating', 'net_rating'])

    def calculate_percentiles(self, model_class, rating_fields):
        queryset = model_class.objects.all()
        for field in rating_fields:
            ratings = list(queryset.order_by(field).values_list(field, flat=True))
            for obj in queryset:
                rating = getattr(obj, field)
                percentile = percentileofscore(ratings, rating, kind='mean')
                setattr(obj, f'{field}_percentile', percentile)
                obj.save(update_fields=[f'{field}_percentile'])
