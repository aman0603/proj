import streamlit as st
from utils.model_utils import get_feature_importance
from utils.plot_utils import plot_feature_importance
import pandas as pd

# Page Title
st.title("Feature Importance")

# Sidebar Options
model_files = {
    "LSTM": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\LSTM_Model_18-11-2024-20-39-11.csv",
    # "Transformers": "data/model_transformers_predictions.csv",
    "TCN": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\TCN_new_model_18-11-2024-23-56-50.csv",
    # "Ensemble": "data/model_ensemble_predictions.csv"
    "CATBOOST": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\catboost_18-11-2024-20-40-27.csv"
}
selected_model = st.sidebar.selectbox(
    "Select a Model for Feature Importance:",
    list(model_files.keys())
)

# Load Original Data
original_data = pd.read_csv("C:/Users/amanp/Desktop/MINOR/proj/code/dataset/Brazil_UF_dengue_monthly.csv")

# Display Feature Importance
if selected_model:
    st.subheader(f"Feature Importance for {selected_model}")
    
    # Compute Feature Importance
    feature_importance = get_feature_importance(original_data, selected_model)
    
    # Plot Feature Importance
    fig = plot_feature_importance(feature_importance)
    st.pyplot(fig)
else:
    st.warning("Please select a model to view feature importance.")
