# Toronto Bike Share Demand Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Latest-green)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-red)

## Project Overview

**Goal:**  
The primary objective of this project is to optimize bike redistribution for the Toronto Bike Share network by predicting hourly demand (`trips_started`) at the station level. Accurate forecasting enables proactive rebalancing of bikes, reducing shortages and ensuring user availability during peak hours.

**Data Sources:**
- **Ridership Data:** Over 10 million trips from Toronto Bike Share (2023–2024).
- **Weather Data:** Historical hourly weather metrics (temperature, precipitation, wind).
- **Station Metadata:** Geospatial coordinates and capacity information.
- **Points of Interest (POI):** Proximity features (e.g., restaurants, transit hubs) enriched via the Geoapify API.

---

## Repository Structure

The project is organized into a modular pipeline for reproducibility and clarity:

### 📂 `Data_Loading_and_Cleaning`
Contains ETL (Extract, Transform, Load) pipelines to ingest raw data.
- **Key Tasks:** Cleaning 'ghost' stations (invalid/test IDs), handling timezone gaps, and standardizing schemas.
- **Files:** `load_bike_stations.py`, `load_weather_data.ipynb`.

### 📂 `Data_Exploration`
Focuses on Exploratory Data Analysis (EDA) and unsupervised learning.
- **`location_features.ipynb`:** Generates spatial clusters and POI features.
- **`final_data_join.ipynb`:** Merges ridership, weather, and location data into the final training set.

### 📂 `Modeling`
Implements feature selection, model training, and evaluation.
- **`3_tree_models.ipynb`:** Implementation of Random Forest and XGBoost ensembles.
- **`4_neural_network.ipynb`:** Deep learning experiments using custom PyTorch architectures.

---

## Methodology

### 1. Data Processing
We implemented a robust cleaning pipeline to handle real-world data issues:
- **Ghost Stations:** Removed test stations and effectively non-operational IDs to reduce noise.
- **Timezone Alignment:** Corrected inconsistencies between UTC weather data and local ridership timestamps.
- **Merging:** Joined disparate datasets on hourly timestamps and station IDs.

### 2. Feature Engineering
A combination of spatial and temporal features drives the model's predictive power:

*   **Spatial Engineering:**
    *   **Clustering:** Applied K-Means (K=5) on station coordinates to group stations into distinct neighborhoods (e.g., Downtown, Scarborough).
    *   **POI Density:** Calculated the density of amenities (restaurants, transit) within a 400m radius using Geoapify.

*   **Temporal Engineering:**
    *   **Cyclical Encoding:** Transformed hours and months into sine/cosine pairs (`hour_sin`, `month_cos`) to preserve cyclic relationships.
    *   **Lag Features:** Introduced lagged demand variables to capture recent trend history.

### 3. Evaluation Strategy
To prevent data leakage, we strictly adhered to a **time-based train/test split**.
- **Split Logic:** We used `day_of_year % 10` to segregate training and testing days, ensuring models predict on unseen future/separate time windows rather than random interactions.
- **Metrics:**
    - **RMSE (Root Mean Squared Error):** Primary metric to penalize large prediction errors.
    - **MAE (Mean Absolute Error):** Secondary metric for interpretability of average error.

---

## Modeling Approach

We benchmarked three distinct modeling paradigms:

1.  **Baseline: Multivariate Linear Regression (MLR)**
    *   Features selected via Lasso Regularization to remove collinearity.
    *   Served as a linear baseline to measure the complexity of the signal.

2.  **Tree Ensembles (Random Forest & XGBoost)**
    *   Chosen for their ability to handle non-linear interactions and robustness to outliers.
    *   **XGBoost** generally provided the best performance, effectively capturing complex demand patterns.

3.  **Deep Learning (Neural Networks)**
    *   **Architecture:** Custom PyTorch models exploring "Wide & Deep" architectures.
    *   **Preprocessing:** `StandardScaler` fitted strictly on training data to avoid look-ahead bias.
    *   **Result:** While promising, NNs required extensive tuning and performed comparably to tree models but with higher computational cost.

---

## Key Results

The Tree-based models (XGBoost and Random Forest) offered the best balance of performance and interpretability. While the Neural Network was competitive, the added complexity did not yield a significant drop in error compared to the optimized XGBoost model.

| Model | Test RMSE | Test R² | Test MAE | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **XGBoost (Best)** | **1.2428** | **0.6126** | **0.5631** | Best overall balance. |
| Random Forest | 1.2493 | 0.6086 | 0.5612 | Very close second. |
| Neural Network | 1.2551 | 0.6050 | 0.5643 | Competitive but complex. |
| Baseline (MLR) | 1.8137 | 0.1751 | 0.8115 | Linear assumption insufficient. |

*Note: RMSE and MAE are in units of "trips started".*

---

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/toronto-bike-share-demand.git
    cd toronto-bike-share-demand
    ```

2.  **Install dependencies:**
    Ensure you have Python 3.9+ installed.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Pipeline:**
    Execute the notebooks in the following order to reproduce results:
    1.  `Data_Loading_and_Cleaning/` (Load raw data)
    2.  `Data_Exploration/location_features.ipynb` (Generate spatial features)
    3.  `Data_Exploration/final_data_join.ipynb` (Create final dataset)
    4.  `Modeling/3_tree_models.ipynb` (Train tree models)
    5.  `Modeling/4_neural_network.ipynb` (Train neural networks)

---

## Contact
**Author:** Andy Hwang 
**Course:** DS3000 - Western University  
**Date:** December 2025
