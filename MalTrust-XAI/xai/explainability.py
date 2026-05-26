# xai/explainability.py
import shap
import matplotlib.pyplot as plt
import os

def generate_shap_explanations(model, X_test):
    """Generate SHAP explanations."""
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    os.makedirs("results/figures", exist_ok=True)
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig("results/figures/shap_summary.png")
    plt.close()
    print("✅ SHAP explanations saved.")