from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

os.environ['PYSPARK_PYTHON'] = 'python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3'

def get_dataframes():
    # Initialize a SparkSession
    # spark = SparkSession.builder \
    #     .appName("Postgres Reader") \
    #     .getOrCreate()
    spark = SparkSession.builder \
    .appName("Postgres Reader") \
    .config("spark.jars", "postgresql-42.6.0.jar") \
    .getOrCreate()

    # Define PostgreSQL connection parameters
    database_url = os.environ.get('DATABASE_URL')
    database_properties = {
        "user": os.environ.get('USER'),
        "password": os.environ.get('PASSWORD'),
        "driver": os.environ.get('DRIVER'),
    }

    # Read data from the PostgreSQL database
    position_player_df = spark.read.jdbc(url=database_url, table="cards_positionplayer", properties=database_properties)
    pitcher_df = spark.read.jdbc(url=database_url, table="cards_pitcher", properties=database_properties)

    return spark, position_player_df, pitcher_df

# Just for testing the function
if __name__ == "__main__":
    spark, position_player_df, pitcher_df = get_dataframes()
    position_player_df.show()
    pitcher_df.show()
    spark.stop()
