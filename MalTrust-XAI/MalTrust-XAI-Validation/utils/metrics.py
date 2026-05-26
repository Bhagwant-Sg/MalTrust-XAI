# utils/metrics.py
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, roc_auc_score, log_loss, brier_score_loss
)

def calculate_all_metrics(y_true, y_pred, y_proba=None, model_name="Model"):
    """
    Calculate comprehensive metrics for binary classification
    """
    metrics = {
        "Model": model_name,
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1": f1_score(y_true, y_pred, zero_division=0),
    }
    
    if y_proba is not None:
        metrics["ROC_AUC"] = roc_auc_score(y_true, y_proba)
        metrics["Log Loss"] = log_loss(y_true, y_proba)
        metrics["Brier Score"] = brier_score_loss(y_true, y_proba)
    
    return pd.DataFrame([metrics])


def save_metrics_table(df, filename="model_metrics.csv"):
    """Save metrics to results/tables/"""
    os.makedirs("results/tables", exist_ok=True)
    path = f"results/tables/{filename}"
    df.to_csv(path, index=False)
    print(f" Metrics saved: {path}")
    return path


def compare_models(models_dict, y_true, y_pred_dict, y_proba_dict=None):
    """Compare multiple models"""
    rows = []
    for name in models_dict:
        y_pred = y_pred_dict[name]
        y_proba = y_proba_dict[name] if y_proba_dict else None
        
        row = {
            "Model": name,
            "Accuracy": accuracy_score(y_true, y_pred),
            "F1": f1_score(y_true, y_pred, zero_division=0),
        }
        if y_proba is not None:
            row["ROC_AUC"] = roc_auc_score(y_true, y_proba)
            row["Log Loss"] = log_loss(y_true, y_proba)
            row["Brier Score"] = brier_score_loss(y_true, y_proba)
        rows.append(row)
    
    return pd.DataFrame(rows)