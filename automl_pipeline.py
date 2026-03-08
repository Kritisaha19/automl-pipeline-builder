import pandas as pd
import os
from pycaret.classification import setup, compare_models, save_model

def run_automl(data_path, target_column):

    # Create models folder if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Load dataset
    data = pd.read_csv(data_path)

    print("Dataset Loaded:")
    print(data.head())

    # Setup PyCaret
    s = setup(data, target=target_column, session_id=123)

    # Train models
    best_model = compare_models()

    # Save model
    save_model(best_model, "models/best_model")

    print("Best model saved successfully.")