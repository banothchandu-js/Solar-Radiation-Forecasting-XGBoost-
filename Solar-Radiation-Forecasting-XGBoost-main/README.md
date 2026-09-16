# ☀️ Solar Radiation & Power Prediction Using XGBoost

## 📌 About the Project

This project uses **Machine Learning and XGBoost** to predict solar radiation and solar power generation using environmental data.

Two real-world datasets are used to study how factors such as **temperature, humidity, wind speed, atmospheric pressure, and cloud cover** affect solar energy.

### 🎯 Predictions

* ☀️ **Solar Radiation** — W/m²
* ⚡ **Generated Power** — kW

## 🧠 Methodology

The project follows these steps:

**Data Collection → Data Cleaning → Statistical Analysis → XGBoost Model → Prediction → Evaluation → Visualization**

## 📊 Input Parameters

* 🌡️ Temperature
* 💧 Humidity
* 🌬️ Wind Speed
* 📈 Atmospheric Pressure
* ☁️ Cloud Cover

## 📈 Model Evaluation

The models are evaluated using:

* **RMSE** — Measures prediction error
* **MAE** — Measures average absolute error
* **R² Score** — Measures how well the model explains the target values

### ☀️ Solar Radiation Results

| Metric |      Result |
| ------ | ----------: |
| RMSE   | 134.52 W/m² |
| MAE    |  87.02 W/m² |
| R²     |       0.643 |

### ⚡ Power Generation Results

| Metric |    Result |
| ------ | --------: |
| RMSE   | 795.96 kW |
| MAE    | 662.73 kW |
| R²     |     0.306 |

## 📈 Visualizations

The project includes:

* 📊 Actual vs Predicted graphs
* 🔍 Feature importance
* 📋 Statistical analysis
* 📈 Model performance results

## 🛠️ Technologies

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 🤖 Scikit-learn
* 🚀 XGBoost
* 📗 OpenPyXL

## 📁 Project Structure

```text
Solar-Radiation-Forecasting-XGBoost/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 dataset/
│   ├── Solar Energy.xlsx
│   └── spg.csv
│
├── 📂 src/
│   ├── dataset1_solar_radiation.py
│   └── dataset2_power_prediction.py
│
├── 📂 results/
│   ├── prediction_output.csv
│   └── graphs/
│
└── 📂 presentation/
    └── Solar-Radiation-and-Power-Prediction-using-XGBoost.pptx
```

## 🌱 Importance of the Project

Accurate solar-energy prediction can help with:

* ⚡ Energy planning
* ☀️ Solar resource assessment
* 🔋 Energy management
* 🌱 Renewable-energy development
* 📊 Data-driven decision making

## 🚀 Future Improvements

Future work could include:

* More environmental parameters
* Time and seasonal information
* Hyperparameter tuning
* Cross-validation
* Comparison with other ML algorithms
* Deep-learning models

## 🎓 Academic Project

**Course:** EI920
**Topic:** Renewable Energy & Machine Learning
**Algorithm:** XGBoost Regression
**Problem Type:** Regression

---

### ☀️ Turning Environmental Data into Solar Energy Insights ⚡
