from bs4 import BeautifulSoup
import requests
import pandas as pd
from cards.models import PositionPlayer, Pitcher
from selenium import webdriver
import os
from django.core.management.base import BaseCommand

# postionplayer table currently has 6 (5 duplicates), pitchers has 4 (3 duplicates). delete the duplicates
# ^ should be done, don't run this again cause it will add more duplicates

def save_data_to_db(csv_filename, model_class):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    csv_filepath = os.path.join(base_dir, 'data', csv_filename)
    
    df = pd.read_csv(csv_filepath)
    df.fillna(0.0, inplace=True)
    df.replace('null', 0.0, inplace=True)
    
    if model_class == PositionPlayer:
        field_mapping = {
            'Name': 'name',
            'Team': 'team',
            'G': 'games',
            'PA': 'plate_appearances',
            'HR': 'home_runs',
            'R': 'runs',
            'RBI': 'runs_batted_in',
            'SB': 'stolen_bases',
            'BB%': 'walk_percentage',
            'K%': 'strikeout_percentage',
            'ISO': 'isolated_power',
            'BABIP': 'babip',
            'AVG': 'avg',
            'OBP': 'obp',
            'SLG': 'slg',
            'wOBA': 'woba',
            'xwOBA': 'xwoba',
            'wRC+': 'wrc_plus',
            'BsR': 'base_running',
            'Off': 'offensive_value',
            'Def': 'defensive_value',
            'WAR': 'war',
            'defense_rating': 'defense_rating',
            'defense_rating_percentile': 'defense_rating_percentile',
            'net_rating': 'net_rating',
            'net_rating_percentile': 'net_rating_percentile',
            'offense_rating': 'offense_rating',
            'offense_rating_percentile': 'offense_rating_percentile',
            'predicted_war': 'predicted_war',
            'war_last_year': 'war_last_year',
            'war_year_before_last': 'war_year_before_last',
        }
    elif model_class == Pitcher:
        field_mapping = {
            'Name': 'name',
            'Team': 'team',
            'W': 'wins',
            'L': 'losses',
            'SV': 'saves',
            'G': 'games',
            'GS': 'games_started',
            'IP': 'innings_pitched',
            'K/9': 'k_per_9',
            'BB/9': 'bb_per_9',
            'HR/9': 'hr_per_9',
            'BABIP': 'babip',
            'LOB%': 'lob_percentage',
            'GB%': 'gb_percentage',
            'HR/FB': 'hr_fb_percentage',
            'vFA (pi)': 'vfa',
            'ERA': 'era',
            'xERA': 'xera',
            'FIP': 'fip',
            'xFIP': 'xfip',
            'WAR': 'war',
            'efficiency_rating': 'efficiency_rating',
            'efficiency_rating_percentile': 'efficiency_rating_percentile',
            'net_rating': 'net_rating',
            'net_rating_percentile': 'net_rating_percentile',
            'performance_rating': 'performance_rating',
            'performance_rating_percentile': 'performance_rating_percentile',
            'predicted_war': 'predicted_war',
            'war_last_year': 'war_last_year',
            'war_year_before_last': 'war_year_before_last',
        }
    
    for index, row in df.iterrows():
        # Create a new dictionary with the mapped field names
        row_dict = {field_mapping.get(col): val for col, val in row.to_dict().items() if col in field_mapping and field_mapping.get(col) is not None}
        
        for key, value in row_dict.items():
            if pd.isnull(value):  # Check if the value is NaN
                row_dict[key] = None  # Set NaN values to None
                
        # Print row_dict to inspect its keys and values
        print(row_dict)
        
        try:
            # Create a new record in the database using the mapped field names
            model_instance = model_class(**row_dict)
            model_instance.save()
        except Exception as e:  # Catch all exceptions
            print(f"Error encountered: {e}")
            print(f"Failed to save row {index}: {row_dict}")

class Command(BaseCommand):
    help = 'Scrape data and save it to the database'

    def handle(self, *args, **kwargs):
        save_data_to_db('hitters.csv', PositionPlayer)
        save_data_to_db('pitchers.csv', Pitcher)