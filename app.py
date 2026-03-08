import streamlit as st
from automl_pipeline import run_automl
import pandas as pd
import os

st.title("AutoML Pipeline Builder")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Dataset Preview")
    st.dataframe(df.head())

    target_column = st.selectbox("Select Target Column", df.columns)

    if st.button("Run AutoML"):

        os.makedirs("data", exist_ok=True)

        dataset_path = "data/uploaded_dataset.csv"
        df.to_csv(dataset_path, index=False)

        run_automl(dataset_path, target_column)

        st.success("AutoML completed! Best model saved.")