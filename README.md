# 🏠 Aqari-Tunisia-Property-Estimator

🔍 Overview

Aqari is a machine learning pipeline designed to predict real estate prices in Tunisia. Built with a philosophy of "Zero rows dropped", the system handles missing values through advanced imputation techniques and manages outliers via Winsorization rather than deletion.

Key Objectives

✅ Preserve all 8,129 property listings without dropping rows

✅ Handle missing values using multivariate imputation strategies

✅ Engineer meaningful features from raw data

✅ Train and compare multiple regression models

✅ Deploy an interactive web application for instant price estimation

📊 Dataset

| **Property**        | **Value**                           |
| ------------------- | ----------------------------------- |
| Source              | dataSetFull.csv                     |
| Total Rows          | 8,129 listings                      |
| Original Features   | 26 columns                          |
| Target Variable     | price_tnd (Price in Tunisian Dinar) |
| Geographic Coverage | 24 Governorates across Tunisia      |


Feature Categories

📍 Location Features

├── governorate, city, location

├── latt, long, distance_to_capital

🏗️ Structural Features 

├── Area, pieces, room, bathroom

├── age, state, garage

✨ Amenities (Binary Flags)
├── garden, concierge, beach_view, mountain_view
├── pool, elevator, furnished, equipped_kitchen
├── central_heating, air_conditioning

💰 Target

└── price_tnd, price_eur

Missing Value Summary (Before Imputation)

| **Feature**        | **Missing Count** | **% Missing** | **Imputation Strategy**          |
| ------------------ | ----------------- | ------------- | -------------------------------- |
| age                | 4,145             | 50.99%        | Median imputation                |
| price_tnd          | 1,708             | 21.01%        | IterativeImputer (BayesianRidge) |
| city               | 1,316             | 16.19%        | Mode per governorate             |
| pieces             | 1,189             | 14.63%        | KNN Imputer (k=5)                |
| state              | 1,100             | 13.53%        | Mode imputation                  |
| bathroom           | 659               | 8.11%         | KNN Imputer (k=5)                |
| room               | 409               | 5.03%         | KNN Imputer (k=5)                |
| Area               | 185               | 2.28%         | KNN Imputer (k=5)                |
| latt/long/distance | 35                | 0.43%         | KNN Imputer (k=5)                |

🌐 Local Deployment

streamlit run HousePredictor.py

Opens at http://localhost:8501

