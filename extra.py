import pandas as pd
import numpy as np

def add_communication_metrics(input_file, output_file):
    # Read the existing CSV file
    df = pd.read_csv(input_file)

    # Set a range for the signal strength and latency
    # Assuming signal strength ranges from 50 to 100 dBm
    # Assuming latency ranges from 100 to 500 ms
    np.random.seed(42)  # For reproducibility
    df['signal_strength'] = np.random.uniform(50, 100, size=len(df))
    df['latency'] = np.random.uniform(100, 500, size=len(df))

    # Write the modified dataframe to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = './satellite_drag_1999.csv'
output_file = './weather_drag_comm-metric.csv'
add_communication_metrics(input_file, output_file)

