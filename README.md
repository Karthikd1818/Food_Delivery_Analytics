# Food Delivery Analytics, Recommendation & Forecasting

An end-to-end Data Science project that analyzes food delivery order data, extracts business insights, validates association rule learning, builds a popularity-based recommendation system, forecasts future revenue using ARIMA, and deploys the recommendation API using FastAPI and Docker.

---

## 📌 Project Overview

This project uses a food delivery dataset containing **3,000 orders** to perform:

* Data loading and exploration
* Data cleaning and preparation
* Exploratory Data Analysis (EDA)
* Food, restaurant, customer, city, and payment analysis
* Association Rule Learning using Apriori
* Popularity-based food recommendation
* Time series revenue forecasting using ARIMA
* REST API development using FastAPI
* Docker containerization

The project demonstrates an end-to-end workflow from raw data analysis to API deployment.

---

## 📂 Dataset

**Dataset:** `food_delivery_analytics_3000.xlsx`

### Features

| Column          | Description                          |
| --------------- | ------------------------------------ |
| `OrderID`       | Unique order identifier              |
| `FoodItem`      | Food ordered                         |
| `TotalAmount`   | Total order amount                   |
| `Restaurant`    | Restaurant associated with the order |
| `CustomerID`    | Customer identifier                  |
| `City`          | Customer/order city                  |
| `PaymentMethod` | Payment method used                  |
| `Rating`        | Customer rating                      |
| `OrderDate`     | Date of the order                    |

---

## 🏗️ Project Structure

```text
Food_delivery_project/
│
├── data/
│   └── food_delivery_analytics_3000.xlsx
│
├── notebook/
│   └── food_delivery_analysis.ipynb
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔍 Project Workflow

```text
Raw Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Cleaning & Preparation
     │
     ▼
Exploratory Data Analysis
     │
     ├── Food Analysis
     ├── Restaurant Analysis
     ├── Customer Analysis
     ├── City Analysis
     ├── Payment Analysis
     └── Rating Analysis
     │
     ▼
Association Rule Learning
     │
     ▼
Recommendation System
     │
     ▼
Time Series Forecasting
     │
     ▼
FastAPI
     │
     ▼
Docker Deployment
```

---

# 1. Data Loading & Exploration

The dataset was loaded using Pandas and examined for:

* Dataset dimensions
* Column names and data types
* Missing values
* Duplicate records
* Unique values
* Numerical statistics
* Categorical distributions

The `OrderDate` column was converted into datetime format for time-series analysis.

---

# 2. Data Cleaning & Preparation

The following preprocessing steps wer
