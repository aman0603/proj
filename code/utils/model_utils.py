import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def calculate_metrics(y_true, y_pred):
    """
    Calculates evaluation metrics: RMSE, MAE, and R².
    """
    return {
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "MAE": mean_absolute_error(y_true, y_pred),
        "R²": r2_score(y_true, y_pred)
    }

def get_feature_importance(original_data, model_name):
    """
    Computes feature importance for the selected model.
    This is a placeholder and should be replaced with model-specific logic.
    """
    features = original_data.columns.drop(["Date", "cases_total"])  # Exclude non-predictive columns
    importance_scores = np.random.rand(len(features))  # Mock importance values
    return pd.DataFrame({"Feature": features, "Importance": importance_scores})
