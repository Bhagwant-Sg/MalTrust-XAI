# features/feature_selection.py
from sklearn.feature_selection import SelectKBest, f_classif
from config.config import EXPERIMENT_CONFIG

def select_features(X, y):
    """Select top features."""
    selector = SelectKBest(score_func=f_classif, k=EXPERIMENT_CONFIG["final_selected_feature_count"])
    X_selected = selector.fit_transform(X, y)
    return X_selected