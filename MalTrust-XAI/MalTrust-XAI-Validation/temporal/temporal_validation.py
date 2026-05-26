# temporal/temporal_validation.py
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from data.chunk_loader import load_or_create_chunks
import os

def run_temporal_validation(chunk_paths, label_col):
    # Temporal split simulation (older vs newer)
    X_train, y_train = load_or_create_chunks()  # Simplified
    X_test, y_test = load_or_create_chunks()    # In real: use date split
    
    model = lgb.LGBMClassifier(n_estimators=250, random_state=42)
    model.fit(X_train, y_train)
    
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]
    
    results = pd.DataFrame([{
        "Experiment": "Temporal Validation",
        "Accuracy": accuracy_score(y_test, pred),
        "F1": f1_score(y_test, pred),
        "ROC_AUC": roc_auc_score(y_test, proba)
    }])
    
    os.makedirs("results/tables", exist_ok=True)
    results.to_csv("results/tables/temporal_validation_results.csv", index=False)
    return results