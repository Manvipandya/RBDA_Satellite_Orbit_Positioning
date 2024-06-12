import pandas as pd
import numpy as np

def calculate_fuel_required(mass, delta_v, specific_impulse):
    """
    Calculate the fuel required for a maneuver using the rocket equation.

    Parameters:
        mass (float): The mass of the satellite in kilograms.
        delta_v (float): The change in velocity in meters per second.
        specific_impulse (float): The specific impulse of the propulsion system in seconds.

    Returns:
        float: The mass of the fuel required in kilograms.
    """
    g0 = 9.81  # Earth's gravitational acceleration near the surface in m/s^2
    return mass * (1 - np.exp(-delta_v / (specific_impulse * g0)))

def process_csv(file_path):
    # Parameters for SAMPLEX satellite
    mass = 1200  # Example mass of SAMPLEX satellite in kg
    specific_impulse = 290  # Example specific impulse in seconds
    force = 1.5  # Example force in newtons
    duration = 500  # Example duration in seconds

    # Load CSV
    df = pd.read_csv(file_path)

    # Calculate averages
    avg_signal_strength = df['signal_strength'].mean()
    avg_latency = df['latency'].mean()

    # Define a function to determine if fuel needs to be calculated
    def check_conditions(row):
        # Calculate delta_v adjusted for drag
        drag_adjusted_delta_v = (force - row['drag_force']) / mass * duration  # Subtract drag_factor from force

        if row['signal_strength'] < avg_signal_strength or row['latency'] > avg_latency:
            return calculate_fuel_required(mass, drag_adjusted_delta_v, specific_impulse)
        return np.nan

    # Apply the function to calculate fuel required
    df['fuel_required'] = df.apply(check_conditions, axis=1)

    # Filter to show only rows where fuel calculation was necessary
    result_df = df.dropna(subset=['fuel_required'])

    # Print the result
    print(result_df.head())
    result_df.to_csv('./fuel_needed', index=False)

# Example usage
process_csv('./weather_drag_comm-metric.csv')

