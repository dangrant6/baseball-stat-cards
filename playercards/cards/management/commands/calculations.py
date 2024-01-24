import pandas as pd
from ...models import Pitcher, PositionPlayer
from decimal import Decimal

# Fetch your model data
pitchers = Pitcher.objects.all()
position_players = PositionPlayer.objects.all()

# Convert to Pandas DataFrames
df_pitchers = pd.DataFrame(list(pitchers.values()))
df_position_players = pd.DataFrame(list(position_players.values()))

def calculate_performance_rating(pitcher):
    return (
        (pitcher.wins * Decimal('1.5')) +
        (pitcher.saves * Decimal('2')) +
        (pitcher.games * Decimal('0.5')) +
        (pitcher.games_started * Decimal('0.5')) +
        (pitcher.innings_pitched * Decimal('0.2')) +
        (pitcher.k_per_9 * Decimal('1'))
    )

def calculate_efficiency_rating(pitcher):
    return (
        (pitcher.bb_per_9 * Decimal('-0.3')) +
        (pitcher.hr_per_9 * Decimal('-0.5')) +
        (pitcher.era * Decimal('-0.5'))
    )

def calculate_net_rating_for_pitcher(pitcher):
    return calculate_performance_rating(pitcher) + calculate_efficiency_rating(pitcher)

def calculate_offense_rating(player):
    return (
        (player.home_runs * Decimal('2')) +
        (player.runs * Decimal('1')) +
        (player.runs_batted_in * Decimal('1')) +
        (player.stolen_bases * Decimal('1.5')) -
        (player.strikeout_percentage * Decimal('0.5')) +
        (player.isolated_power * Decimal('2')) +
        (player.avg * Decimal('100')) +
        (player.obp * Decimal('100')) +
        (player.slg * Decimal('100')) +
        (player.woba * Decimal('100')) +
        (player.wrc_plus * Decimal('0.5')) +
        (player.base_running * Decimal('0.5')) +
        (player.offensive_value * Decimal('1'))
    )

def calculate_defense_rating(player):
    return player.defensive_value * Decimal('1')

def calculate_net_rating_for_player(player):
    return calculate_offense_rating(player) - calculate_defense_rating(player)


# Calculate ratings
df_position_players['offense_rating'] = df_position_players.apply(calculate_offense_rating, axis=1)
df_position_players['defense_rating'] = df_position_players.apply(calculate_defense_rating, axis=1)
df_position_players['net_rating'] = df_position_players.apply(calculate_net_rating_for_player, axis=1)

# Calculate percentiles for each rating
df_position_players['offense_percentile'] = df_position_players['offense_rating'].rank(pct=True)
df_position_players['defense_percentile'] = df_position_players['defense_rating'].rank(pct=True)
df_position_players['net_percentile'] = df_position_players['net_rating'].rank(pct=True)

# Calculate ratings
df_pitchers['performance_rating'] = df_pitchers.apply(calculate_performance_rating, axis=1)
df_pitchers['efficiency_rating'] = df_pitchers.apply(calculate_efficiency_rating, axis=1)
df_pitchers['net_rating'] = df_pitchers.apply(calculate_net_rating_for_pitcher, axis=1)

# Calculate percentiles for each rating
df_pitchers['performance_percentile'] = df_pitchers['performance_rating'].rank(pct=True)
df_pitchers['efficiency_percentile'] = df_pitchers['efficiency_rating'].rank(pct=True)
df_pitchers['net_percentile'] = df_pitchers['net_rating'].rank(pct=True)
