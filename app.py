from fastapi import FastAPI, HTTPException
import pandas as pd


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

DATA_PATH = "data/food_delivery_analytics_3000.xlsx"

df = pd.read_excel(DATA_PATH)


# --------------------------------------------------
# Prepare Recommendation Data
# --------------------------------------------------

food_stats = (
    df.groupby("FoodItem")
      .agg(
          Orders=("OrderID", "count"),
          Revenue=("TotalAmount", "sum"),
          AverageRating=("CustomerRating", "mean")
      )
      .reset_index()
)

food_stats = food_stats.sort_values(
    by=["Orders", "AverageRating"],
    ascending=[False, False]
)


# --------------------------------------------------
# Create FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Food Delivery Recommendation API",
    description="Food recommendation API based on historical popularity and ratings.",
    version="1.0.0"
)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Food Delivery Recommendation API is running"
    }


# --------------------------------------------------
# Popular Food Endpoint
# --------------------------------------------------

@app.get("/popular")
def popular_foods(limit: int = 5):

    if limit < 1:
        raise HTTPException(
            status_code=400,
            detail="Limit must be greater than 0."
        )

    recommendations = food_stats.head(limit)

    return recommendations.to_dict(orient="records")


# --------------------------------------------------
# Recommendation Endpoint
# --------------------------------------------------

@app.get("/recommend/{food_item}")
def recommend_food(food_item: str, limit: int = 5):

    matched_food = food_stats[
        food_stats["FoodItem"].str.lower() == food_item.lower()
    ]

    if matched_food.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Food item '{food_item}' not found."
        )

    # Since each OrderID contains only one FoodItem,
    # Apriori cannot provide item-to-item associations.
    # Therefore, recommendations are based on popular
    # food items from the historical dataset.

    recommendations = food_stats[
        food_stats["FoodItem"].str.lower() != food_item.lower()
    ].head(limit)

    return {
        "requested_food": food_item,
        "recommendation_method": "Popularity-based",
        "recommendations": recommendations.to_dict(orient="records")
    }