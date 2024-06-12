import pandas as pd
import numpy as np


# For a text file with space as delimiter
hasdm1 = pd.read_csv('/Users/manvi/Downloads/2000_HASDM_500-575KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm2 = pd.read_csv('/Users/manvi/Downloads/2000_HASDM_400-475KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm3 = pd.read_csv('/Users/manvi/Downloads/2001_HASDM_500-575KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm4 = pd.read_csv('/Users/manvi/Downloads/2001_HASDM_400-475KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm5 = pd.read_csv('/Users/manvi/Downloads/2002_HASDM_500-575KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm6 = pd.read_csv('/Users/manvi/Downloads/2002_HASDM_400-475KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm7 = pd.read_csv('/Users/manvi/Downloads/2003_HASDM_500-575KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm8 = pd.read_csv('/Users/manvi/Downloads/2003_HASDM_400-475KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm9 = pd.read_csv('/Users/manvi/Downloads/2004_HASDM_500-575KM.set.txt', sep='\s+', engine='python', skiprows=19)
hasdm10 = pd.read_csv('/Users/manvi/Downloads/2004_HASDM_400-475KM.set.txt', sep='\s+', engine='python', skiprows=19)

hasdm = pd.concat([hasdm1, hasdm2, hasdm3, hasdm4, hasdm5, hasdm6, hasdm7, hasdm8, hasdm9, hasdm10], ignore_index=True)
hasdm.to_csv('/Users/manvi/Downloads/merged_hasdm.csv', index=False)
hasdm = hasdm.rename(columns={'LON': 'longitude', 'LAT': 'latitude', '#YYYMMDDhhmm': 'timestamp'})
hasdm.to_csv('/Users/manvi/Downloads/merged_hasdm.csv', index=False)

hasdm['longitude'] = (hasdm['longitude'] / 10).round() * 10
# Convert timestamps to a common format
#sat_hourly['timestamp'] = pd.to_datetime(sat_hourly['timestamp'], utc=True)
hasdm['timestamp'] = pd.to_datetime(hasdm['timestamp'], format='%Y%m%d%H%M', utc=True)