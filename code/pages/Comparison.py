import streamlit as st
import pandas as pd
# from utils.model_utils import calculate_metrics
from utils.plot_utils import plot_metrics_comparison, plot_actual_vs_predicted,plot_feature_comparison,plot_department_metrics

# Page Title
st.title("Model Comparison")

# Sidebar Options
model_files = {
    "LSTM": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\LSTM_Model_18-11-2024-20-39-11.csv",
    # "Transformers": "data/model_transformers_predictions.csv",
    "TCN": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\TCN_new_model_18-11-2024-23-56-50.csv",
    # "Ensemble": "data/model_ensemble_predictions.csv"
    "CATBOOST": r"C:\Users\amanp\Desktop\MINOR\proj\code\metrics\Brazil\catboost_18-11-2024-20-40-27.csv"
}
model_options = st.sidebar.multiselect(
    "Select Models for Comparison:",
    list(model_files.keys()),
    default=["LSTM", "TCN"]
)

# metric_selection = st.sidebar.radio(
#     "Metrics to Compare:",
#     ("Minimum", "Maximum", "All")
# )

# Load Original Data
original_data = pd.read_csv("C:/Users/amanp/Desktop/MINOR/proj/code/dataset/Brazil_UF_dengue_monthly.csv")

# Sidebar for Feature Selection
selected_feature = st.sidebar.selectbox(
    "Select a Feature to Compare Across Models:",
    [
        "NRMSE 0-19 Training",
        "NRMSE All Training",
        "NRMSE 0-19 Validation",
        "NRMSE All Validation",
        "MAE (DengRate_all) Val",
        "MAE (DengRate_019) Val"
    ]
)

if model_options:
    st.subheader("Model Performance Comparison")
    
    # Metrics Computation
    feature_results = {}
    for model in model_options:
        model_data = pd.read_csv(model_files[model])
        
        # Store selected feature metric
        feature_results[model] = model_data[selected_feature].mean()  # Compute mean value for the feature
    
    # Plot Feature Comparison
    st.subheader(f"Comparison of {selected_feature} Across Models")
    feature_fig = plot_feature_comparison(feature_results, selected_feature)
    st.pyplot(feature_fig)

    # Select Model for Department-Wise Breakdown
    st.subheader("Department-Wise Analysis")
    selected_model = st.selectbox("Select a model to view department-specific metrics:", model_options)
    
    department_fig = plot_department_metrics(pd.read_csv(model_files[selected_model]), selected_feature)
    st.pyplot(department_fig)
else:
    st.warning("Please select at least one model for comparison.")

