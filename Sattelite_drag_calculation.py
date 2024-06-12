import pandas as pd

# Load the dataset
file_path = './predicted_rho.csv'  # Adjust the path to your actual file location
data = pd.read_csv(file_path)

# Define the function to calculate drag force
def calculate_satellite_drag(C_d, A, rho, v):
    """
    Calculate the drag force on a satellite using the formula:
    F_drag = 0.5 * C_d * A * rho * v^2

    Parameters:
    C_d (float): Drag coefficient of the satellite.
    A (float): Cross-sectional area of the satellite (m^2).
    rho (float): Atmospheric density at the satellite's altitude (kg/m^3).
    v (float): Satellite's orbital velocity (m/s).

    Returns:
    float: Drag force in Newtons (N).
    """
    F_drag = 0.5 * abs(float(C_d)) * A * float(rho) * v**2
    return F_drag

# Constants for the calculation
A = 1.7  # Cross-sectional area in square meters
v = 7500  # Approximate orbital velocity in m/s for low Earth orbit

# Apply the function to all rows in the dataset to calculate drag forcex
data['drag_force'] = data.apply(lambda row: calculate_satellite_drag(2, A, row['Predicted_RHO'], v), axis=1)

# Save the updated dataset to a new CSV file
updated_file_path = './satellite_drag_1999.csv'
data.to_csv(updated_file_path, index=False)

print(f"Updated dataset with drag force saved successfully to {updated_file_path}")
