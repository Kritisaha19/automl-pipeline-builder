import pandas as pd
from pycaret.classification import setup, compare_models, save_model


def run_automl(data_path, target_column):

    # Load dataset
    data = pd.read_csv(data_path)

    print("Dataset Loaded:")
    print(data.head())

    # Setup PyCaret environment
    s = setup(data, target=target_column, session_id=123)

    # Compare models automatically
    best_model = compare_models()

    # Save best model
    save_model(best_model, "models/best_model")

    print("Best model saved successfully.")