import pandas as pd
import joblib

# Read the CSV file into a DataFrame
csv_path = './SX_K0_30F_1106906.csv'
original_data_df = pd.read_csv(csv_path)

# Rename columns
original_data_df.rename(columns={
    original_data_df.columns[0]: 'timestamp',
    original_data_df.columns[8]: 'DIPOLE_CENTER_X_km',
    original_data_df.columns[10]: 'DIPOLE_CENTER_Y_km',
    original_data_df.columns[12]: 'DIPOLE_CENTER_Z_km'
}, inplace=True)

# Delete unwanted columns
original_data_df.drop(columns=[original_data_df.columns[9], original_data_df.columns[11], original_data_df.columns[13], original_data_df.columns[15], original_data_df.columns[16], original_data_df.columns[17]], inplace=True)
original_data_df['timestamp'] = pd.to_datetime(original_data_df['timestamp'])
original_data_df.set_index('timestamp', inplace=True)

variables_to_include = ['EXOS_TEMP__Kelvin', 'MX_(@_Mx_)_Gauss_RE**3', 'MY_(@_My_)_Gauss_RE**3',
                        'MZ_(@_Mz_)_Gauss_RE**3', 'DIPOLE_CENTER_X_km', 'DIPOLE_CENTER_Y_km', 'DIPOLE_CENTER_Z_km']

filtered_data_df = original_data_df[variables_to_include]

loaded_model = joblib.load('./RHO_model.pkl')
rho_predictions = loaded_model.predict(filtered_data_df)

# Add predictions as a new column to the new dataset
original_data_df['Predicted_RHO'] = rho_predictions

# Save the modified dataset back to a new CSV file
original_data_df.to_csv('./predicted_rho.csv', index=False)

print("New dataset with Predicted_RHO values saved.")
