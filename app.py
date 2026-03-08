import streamlit as st
import pandas as pd
from automl_pipeline import run_automl
import os

st.title("AutoML Pipeline Builder")

st.write("Upload a dataset and automatically train machine learning models.")

# Upload dataset
uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file is not None:

    # Save uploaded file
    dataset_path = os.path.join("data", "uploaded_dataset.csv")
    os.makedirs("data", exist_ok=True)

    with open(dataset_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load dataset
    data = pd.read_csv(dataset_path)

    st.subheader("Dataset Loaded")
    st.dataframe(data)

    # Select target column
    target_column = st.selectbox("Select Target Column", data.columns)

    # Run AutoML
    if st.button("Run AutoML"):

        leaderboard = run_automl(dataset_path, target_column)

        st.success("AutoML completed! Best model saved.")

        # Show leaderboard
        st.subheader("Model Leaderboard")
        st.dataframe(leaderboard)

        # Download model
        model_path = "models/best_model.pkl"

        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                st.download_button(
                    label="Download Best Model",
                    data=f,
                    file_name="best_model.pkl"
                )