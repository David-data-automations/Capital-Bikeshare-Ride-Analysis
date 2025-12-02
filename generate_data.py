import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# --- 1. SETUP ---
# Create 'datasets' folder if it doesn't exist (where notebook expects data)
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# Define core parameters and data size (e.g., 20,000 trips)
N = 20000
start_date = datetime(2023, 7, 1)
end_date = datetime(2023, 8, 31)
date_range = [start_date + timedelta(seconds=np.random.randint(0, (end_date - start_date).total_seconds())) for _ in range(N)]

# Define a list of simulated station names
station_names = [f'Station_{i:02d}' for i in range(1, 51)]
popular_stations = station_names[:10] # Top 10 are more popular

# --- 2. GENERATE CORE DATA FRAME ---
df = pd.DataFrame({'started_at': date_range})

# Simulate User Types (Registered vs. Casual)
# Registered users typically make up 60-70% of rides
df['member_casual'] = np.random.choice(
    ['member', 'casual'], 
    N, 
    p=[0.65, 0.35]
)

# Simulate Ride Durations (Seconds) - skewed toward short trips
df['ride_length'] = np.random.lognormal(mean=7.5, sigma=1.0, size=N).astype(int)
df['ride_length'] = np.clip(df['ride_length'], a_min=60, a_max=7200) # Min 1 min, Max 2 hours

# Simulate Start and End Stations
df['start_station_name'] = np.random.choice(
    station_names, 
    N, 
    p=np.append(np.repeat(0.04, 10), np.repeat(0.012, 40)) # Popular stations get more traffic
)
# Ensure end station is usually different from start station (80% chance)
df['end_station_name'] = [
    np.random.choice(station_names) if np.random.rand() < 0.8 else start
    for start in df['start_station_name']
]

# Simulate Geo-Coordinates (simple simulation around a central point)
center_lat, center_lon = 38.9072, -77.0369
df['start_lat'] = center_lat + np.random.uniform(-0.05, 0.05, N)
df['start_lng'] = center_lon + np.random.uniform(-0.05, 0.05, N)
df['end_lat'] = center_lat + np.random.uniform(-0.05, 0.05, N)
df['end_lng'] = center_lon + np.random.uniform(-0.05, 0.05, N)


# --- 3. SAVE FILE ---
# Rename and reorder columns to mimic common public datasets
df['ended_at'] = df['started_at'] + pd.to_timedelta(df['ride_length'], unit='s')
df['ride_id'] = [f'R{i:05d}' for i in range(N)]

final_cols = ['ride_id', 'member_casual', 'ride_length', 'started_at', 'ended_at', 
              'start_station_name', 'end_station_name', 'start_lat', 'start_lng', 
              'end_lat', 'end_lng']
df = df[final_cols]

df.to_csv('datasets/bikeshare_trips_simulated.csv', index=False)
print("Generated dummy data file successfully in the 'datasets/' folder.")
