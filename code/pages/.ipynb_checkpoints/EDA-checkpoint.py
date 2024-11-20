import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_data
from utils.plot_utils import plot_temporal_trends, plot_correlation_matrix

# Page Title
st.title("Exploratory Data Analysis (EDA)")

# Load Data
data = load_data()

# Sidebar Options
eda_option = st.sidebar.radio(
    "Select EDA Option:",
    ("Temporal Trends", "Correlation Matrix")
)

# Temporal Trends Visualization
if eda_option == "Temporal Trends":
    st.subheader("Temporal Trends Visualization")
    
    # Relevant features for temporal trends
    relevant_features = [
         'cases_total', 'cases0_19', 
         'cases20_99','NDVI_d', 'dewpoint_temperature_2m_d', 'humidity_d', 
         'max_temperature_2m_d', 'min_temperature_2m_d', 'temperature_2m_d',
         'total_precipitation_d'
    ]
    
    # Ensure only relevant features from the dataset are displayed
    selectable_features = [col for col in relevant_features if col in data.columns]
    
    # Dropdown to select a feature for temporal trends
    selected_column = st.selectbox(
        "Select a column for temporal analysis:", 
        options=selectable_features
    )
    
    if selected_column:
        # Plot and display the trend
        fig = plot_temporal_trends(data, selected_column)
        st.pyplot(fig)
    else:
        st.warning("No relevant features available for temporal trends.")


# Correlation Matrix Visualization
elif eda_option == "Correlation Matrix":
    st.subheader("Correlation Matrix")
    
    # Predefined numeric features for correlation analysis
    predefined_features = [
        'NDVI_d', 'dewpoint_temperature_2m_d', 'humidity_d', 
        'max_temperature_2m_d', 'min_temperature_2m_d', 'temperature_2m_d',
        'surface_pressure_d', 'total_precipitation_d', 
        'Pop0_19_Urban_UF', 'PopTotal_Urban_UF', 'cases_total', 
        'max_elevation_d', 'mean_elevation_d', 'stdDev_elevation_d', 
        'ivs', 'idhm', 'renda_per_capita', 'Forest_Cover_Percent'
    ]
    
    # Ensure only the predefined features are displayed
    selectable_features = [col for col in predefined_features if col in data.columns]
    
    # Multiselect for predefined features
    selected_columns = st.multiselect(
        "Select columns for correlation analysis:",
        options=selectable_features,  # Only allow predefined features
        default=selectable_features[:5]  # Pre-select the first 5 predefined features
    )
    
    # Check if user selected columns
    if selected_columns:
        # Filter numeric columns from the predefined selection
        numeric_data = data[selected_columns]
        if numeric_data.empty:
            st.error("No numeric columns selected. Please select at least one numeric column.")
        else:
            # Plot and display the correlation matrix
            fig = plot_correlation_matrix(numeric_data)
            st.pyplot(fig)
    else:
        st.warning("Please select at least one column.")


