# MalTrust-XAI
**If you want to run the entire framework in the single notebook then use the "framework-development-20-05-2026.ipynb" this file is represent the Framework Development", and then this file "revised-article-results.ipynb" represent the Supporting Additional Validation of the Experimentation, then you just need to run the cell and wait for the code to process, if you want to debug the entire framework step by step and check the entire analysis fromteh intial stage to the final stage they can use the "MalTrust-XAI" folder as in that folder the both codes are breakdown in the chunks and modules for the better understanding. {Note: For the ease of implementation and computation effective use the Kaggle Notebook, and use the EMBER2024, and BODMASS Dataset as input for all the experiments, then they will run smoothly.}**

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
   
