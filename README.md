# MalTrust-XAI

**An Explainable Hybrid Artificial Intelligence Framework for Malware Detection with Blockchain-Assisted Integrity Validation**

---

##  Project Overview

**MalTrust-XAI** is a complete end-to-end framework for **binary malware detection** on the **EMBER2024 Win64** dataset. 

It combines:
- Scalable data processing from large JSONL files
- Advanced feature engineering from PE files
- Multiple baseline machine learning models
- Explainable AI (XAI) techniques
- Comprehensive evaluation and visualization

The framework supports both **debug mode** (small subset) and **final mode** (≈500,000 samples using 25 training files).

---

##  Key Features

- **Modular Architecture** – Clean separation of concerns
- **Scalable Data Loading** – Handles multiple large JSONL files efficiently
- **Rich Feature Engineering** – General, header, imports, strings, histogram, etc.
- **Baseline Models** – RandomForest, XGBoost, LightGBM
- **Explainable AI** – SHAP explanations and feature importance
- **Reproducible Results** – Full logging, saved models, figures, and tables
- **Config-Driven** – Easy switching between debug and final runs

---

##  Project Structure

```bash
MalTrust-XAI/
├── README.md
├── requirements.txt
├── main.py                    # Entry point
├── config/
│   └── config.py
├── data/
│   ├── __init__.py
│   └── data_loader.py
├── features/
│   ├── __init__.py
│   ├── feature_engineering.py
│   └── feature_selection.py
├── models/
│   ├── __init__.py
│   ├── baseline_models.py
│   └── train.py
├── xai/
│   ├── __init__.py
│   └── explainability.py
├── utils/
│   ├── __init__.py
│   └── visualization.py
├── results/
│   ├── figures/               # Accuracy charts, SHAP plots, etc.
│   └── tables/                # Performance CSVs
└── notebooks/
   
