import json
import pandas as pd

# Read the JSON file
with open('./FinalProject/data/bike_stations.json', 'r') as f:
    data = json.load(f)

stations = data['data']['stations']
df = pd.DataFrame(stations)

df_subset = df[['station_id', 'name', 'physical_configuration', 'lat', 'lon', 'capacity', 'address', 'is_charging_station', 'nearby_distance']]

df_subset.to_csv('bike_stations.csv', index=False)

print(f"Saved {len(df)} stations to bike_stations.csv")

