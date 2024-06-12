import pandas as pd
import numpy as np
import csv

with open('/Users/manvi/Downloads/SX_K0_30F_3349923.csv', 'r') as file:
    first_line = file.readline().strip()

# Split the first line based on commas to get the original column names
original_columns = first_line.split(',')

updated_cols = []

for i, col in enumerate(original_columns):
    if i ==0: 
        original_columns[i] = 'timestamp'
    elif i ==1:
        original_columns[i] = 'HTM'
    elif i == 17: 
        original_columns[i] = 'longitude'
    elif i == 18:
        original_columns[i] = 'latitude'
    elif i == 34:
        original_columns[i] = 'DIPOLE_CENTER_X_km'
        del original_columns[35]
    elif i == 35:
        original_columns[i] = 'DIPOLE_CENTER_Y_km'
        del original_columns[36]
    elif i == 36:
        original_columns[i] = 'DIPOLE_CENTER_Z_km'
        del original_columns[37]
    elif i in [37, 38, 39, 40]:
        original_columns[i] = 'ME_' + original_columns[i]
    elif i in [45, 46, 47, 48]:
        original_columns[i] = 'S100_' + original_columns[i]
    elif i in [41, 42, 43, 44]:
        original_columns[i] = 'N100_' + original_columns[i]
    #print(i,col)
    
    
# Read the CSV file
with open('/Users/manvi/Downloads/SX_K0_30F_3349923.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Update the first row with the new array
rows[0] = original_columns

# Write the updated data back to the CSV file
with open('/Users/manvi/Downloads/SX_K0_30F_3349923_updated.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

