import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Load your dataset
df = pd.read_csv("./weather_drag_comm-metric.csv")

# Perform data transformation (Z-score normalization)
for column in df.columns:
    if column != 'signal_strength' and column != 'latency':
        mean = df[column].mean()
        std_dev = df[column].std()
        df[column] = (df[column] - mean) / std_dev

# Calculate cross-correlation between all variables and the target variables
correlations_signal_strength = {}
correlations_latency = {}

for column in df.columns:
    if column not in ['signal_strength', 'latency']:
        correlation_signal_strength, _ = pearsonr(df[column], df['signal_strength'])
        correlation_latency, _ = pearsonr(df[column], df['latency'])
        correlations_signal_strength[column] = correlation_signal_strength
        correlations_latency[column] = correlation_latency

# Print correlations with Signal Strength
print("Correlations with Signal Strength:")
for column, correlation in correlations_signal_strength.items():
    print(f"{column}: {correlation}")

# Print correlations with Latency
print("\nCorrelations with Latency:")
for column, correlation in correlations_latency.items():
    print(f"{column}: {correlation}")
    
    
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
X = df.drop(columns=['signal_strength', 'latency'])
y_signal_strength = df['signal_strength']
y_latency = df['latency']

# Split the data into training and testing sets
X_train, X_test, y_train_signal_strength, y_test_signal_strength = train_test_split(X, y_signal_strength, test_size=0.2, random_state=42)
X_train, X_test, y_train_latency, y_test_latency = train_test_split(X, y_latency, test_size=0.2, random_state=42)

# Apply PCA
pca = PCA(n_components=0.95)  # Retain 95% of the variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train linear regression models
model_signal_strength = LinearRegression()
model_latency = LinearRegression()

model_signal_strength.fit(X_train_pca, y_train_signal_strength)
model_latency.fit(X_train_pca, y_train_latency)

# Predict on the test set
y_pred_signal_strength = model_signal_strength.predict(X_test_pca)
y_pred_latency = model_latency.predict(X_test_pca)

# Calculate RMSE (Root Mean Squared Error)
rmse_signal_strength = mean_squared_error(y_test_signal_strength, y_pred_signal_strength, squared=False)
rmse_latency = mean_squared_error(y_test_latency, y_pred_latency, squared=False)

print("RMSE for Signal Strength prediction:", rmse_signal_strength)
print("RMSE for Latency prediction:", rmse_latency)

import joblib

# Save the model
joblib.dump(model_signal_strength, './signal_model.pkl')
joblib.dump(model_latency, './latency_model.pkl')
