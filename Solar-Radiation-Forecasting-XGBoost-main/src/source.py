# ==============================
# SOLAR ENERGY ML PROJECT (XGBOOST)
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

# ==============================
# 1. LOAD DATASET
# ==============================

file_path = r"C:\Users\malot\OneDrive\Documents\Solar Energy.xlsx"

data = pd.read_excel(file_path)

print("\n✅ Dataset Loaded Successfully!\n")
print("Columns in dataset:\n", data.columns)

# ==============================
# 2. COLUMN SELECTION (AUTO SAFE)
# ==============================

columns_map = {
    'temp': ['temp', 'temperature'],
    'humidity': ['humidity'],
    'windspeed': ['windspeed', 'wind_speed'],
    'pressure': ['sealevelpressure', 'pressure'],
    'cloud': ['cloudcover', 'cloud'],
    'radiation': ['solarradiation']
}

def find_column(possible_names):
    for name in possible_names:
        if name in data.columns:
            return name
    return None

temp_col = find_column(columns_map['temp'])
hum_col = find_column(columns_map['humidity'])
wind_col = find_column(columns_map['windspeed'])
press_col = find_column(columns_map['pressure'])
cloud_col = find_column(columns_map['cloud'])
rad_col = find_column(columns_map['radiation'])

selected_cols = [temp_col, hum_col, wind_col, press_col, cloud_col, rad_col]
selected_cols = [col for col in selected_cols if col is not None]

data = data[selected_cols]

print("\n✅ Selected Columns:\n", selected_cols)

# ==============================
# 3. DATA CLEANING
# ==============================

data = data.dropna()

print("\n✅ Missing values removed!")
print("Remaining rows:", len(data))

# ==============================
# 4. FIX NEGATIVE TEMPERATURE
# ==============================

# ==============================
# 5. STATISTICAL ANALYSIS
# ==============================

print("\n===== STATISTICAL RESULTS =====")

print("\n🔹 Minimum Values:\n", data.min())
print("\n🔹 Maximum Values:\n", data.max())
print("\n🔹 Standard Deviation:\n", data.std())

# ==============================
# 6. INPUT & OUTPUT SPLIT
# ==============================

X = data.drop(columns=[rad_col])
y = data[rad_col]

# ==============================
# 7. TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 8. XGBOOST MODEL
# ==============================

model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5
)

model.fit(X_train, y_train)

print("\n✅ Model Training Completed!")

# ==============================
# 9. PREDICTION
# ==============================

y_pred = model.predict(X_test)

# ==============================
# 10. MODEL PERFORMANCE
# ==============================

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
from sklearn.metrics import mean_absolute_error, r2_score
# MAE
mae = mean_absolute_error(y_test, y_pred)
# R² Score
r2 = r2_score(y_test, y_pred)
print("\n📊 MAE:", mae)
print("📊 R² Score:", r2)
print("\n📊 RMSE:", rmse)

# ==============================
# 11. GRAPH
# ==============================

plt.figure()
plt.plot(y_test.values, label="Actual")
plt.plot(y_pred, label="Predicted")
plt.legend()
plt.title("Actual vs Predicted Solar Radiation")
plt.xlabel("Data Points")
plt.ylabel("Solar Radiation (W/m²)")
plt.show()

# ==============================
# 12. SAVE OUTPUT
# ==============================

output_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

output_df.to_csv("prediction_output.csv", index=False)

print("\n✅ Output saved as 'prediction_output.csv'")
