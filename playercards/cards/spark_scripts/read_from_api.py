from pyspark.sql import SparkSession
import requests

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("API Reader") \
    .getOrCreate()

# Fetch data from the API
response_position_player = requests.get("http://localhost:8000/api/positionplayers/")
response_pitcher = requests.get("http://localhost:8000/api/pitchers/")

# Check if the request was successful and parse JSON data
if response_position_player.status_code == 200 and response_pitcher.status_code == 200:
    data_position_player = response_position_player.json()
    data_pitcher = response_pitcher.json()

    # Create Spark DataFrames from the JSON data
    position_player_df = spark.createDataFrame(data_position_player)
    pitcher_df = spark.createDataFrame(data_pitcher)
    
    # Show the data (just as an example, you might want to do more complex operations)
    position_player_df.show()
    pitcher_df.show()
else:
    print("Failed to fetch data from API")

# Stop the SparkSession
spark.stop()
