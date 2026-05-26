# models/baseline_models.py
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb

def get_baseline_models():
    """Return dictionary of baseline models."""
    return {
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        "XGBoost": xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, random_state=42, n_jobs=-1),
        "LightGBM": lgb.LGBMClassifier(n_estimators=200, learning_rate=0.1, random_state=42, n_jobs=-1),
    }