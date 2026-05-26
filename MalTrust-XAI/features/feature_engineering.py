# features/feature_engineering.py
import pandas as pd

def extract_features(df):
    """Extract features from EMBER2024 JSONL data."""
    # Example: Flatten general, header, etc.
    features = pd.DataFrame()

    if 'general' in df.columns:
        general_df = pd.DataFrame(df['general'].apply(pd.Series))
        features = pd.concat([features, general_df], axis=1)

    if 'header' in df.columns:
        # Add more complex feature extraction here
        pass

    # Add more feature groups as needed (imports, strings, histogram, etc.)
    features['label'] = df['label']
    return features.drop(columns=['label'], errors='ignore'), features['label']