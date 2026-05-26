# models/train.py
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import joblib
import os
from data.data_loader import load_train_files
from features.feature_engineering import extract_features
from models.baseline_models import get_baseline_models

def train_baseline_models(train_files):
    """Train all baseline models."""
    models = get_baseline_models()
    results = {}

    for file_path in tqdm(train_files, desc="Training on files"):
        df = pd.read_json(file_path, lines=True)
        X, y = extract_features(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.15, random_state=42, stratify=y
        )

        for name, model in models.items():
            model.fit(X_train, y_train)
            pred = model.predict(X_test)

            acc = accuracy_score(y_test, pred)
            f1 = f1_score(y_test, pred, average='binary')

            if name not in results:
                results[name] = {"accuracy": acc, "f1": f1}
            else:
                # Average across files
                results[name]["accuracy"] = (results[name]["accuracy"] + acc) / 2
                results[name]["f1"] = (results[name]["f1"] + f1) / 2

    # Save trained models
    os.makedirs("results", exist_ok=True)
    joblib.dump(models, "results/trained_models.pkl")

    return results