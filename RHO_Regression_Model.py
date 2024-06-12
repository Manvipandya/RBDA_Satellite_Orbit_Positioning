import pandas as pd

# Load the dataset
file_path = './merged_final_dataset_with_outliers.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure and columns
data.head(), data.columns

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr


# Load the dataset
df = pd.read_csv('./merged_final_dataset_with_outliers.csv')

# Define the index of the timestamp column
timestamp_column_index = 1

# Extract the final variable
final_variable = df.iloc[:, -1]

# Exclude the timestamp column and the final column (final variable)
variables_to_analyze = df.drop(columns=[df.columns[timestamp_column_index], df.columns[-1]])

# Loop through each variable in the dataset
for column in variables_to_analyze.columns:
    # Extract the current variable
    current_variable = variables_to_analyze[column]

    # Calculate the cross-correlation using Pearson correlation coefficient
    correlation_coefficient, _ = pearsonr(current_variable, final_variable)

    # Print the correlation coefficient
    print(f"Correlation between {column} and final variable: {correlation_coefficient}")

# Selected features based on their correlation coefficients
selected_features = ['EXOS_TEMP__Kelvin', 'MX_(@_Mx_)_Gauss_RE**3', 'MY_(@_My_)_Gauss_RE**3',
                     'MZ_(@_Mz_)_Gauss_RE**3', 'DIPOLE_CENTER_X_km', 'DIPOLE_CENTER_Y_km', 'DIPOLE_CENTER_Z_km']

# Create a new DataFrame with selected features
new_df = df[selected_features].copy()


# Define a function to perform z-score normalization
def z_score_normalization(column):
    mean = column.mean()
    std_dev = column.std()
    normalized_column = (column - mean) / std_dev
    return normalized_column

# Apply z-score normalization to all columns except the final variable
transformed_data = new_df.apply(z_score_normalization)

# Create a new DataFrame with the transformed data
transformed_df = pd.DataFrame(transformed_data)

# Split the dataset into features (X) and target variable (y)
X = transformed_df
y = df.iloc[:, -1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=0.95)  # Retain 95% of variance
#X_train_pca = pca.fit_transform(X_train)
#X_test_pca = pca.transform(X_test)

# Fit a linear regression model
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Predict on the testing set
y_pred = regression_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


import joblib

# Save the model
joblib.dump(regression_model, './RHO_model.pkl')

