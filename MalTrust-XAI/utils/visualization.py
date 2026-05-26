# utils/visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import os

def save_final_visualizations(results):
    """Save all final figures and tables."""
    os.makedirs("results/figures", exist_ok=True)
    os.makedirs("results/tables", exist_ok=True)

    # Accuracy Comparison
    models = list(results.keys())
    accuracies = [results[m]["accuracy"] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, accuracies, color=['blue', 'green', 'orange'])
    plt.title("Baseline Models Accuracy Comparison (500k samples)")
    plt.ylabel("Accuracy")
    plt.ylim(0.9, 1.0)
    plt.savefig("results/figures/baseline_accuracy_comparison.png")
    plt.close()

    # Save results as CSV
    pd.DataFrame(results).T.to_csv("results/tables/model_performance.csv")

    print(" All visualizations and tables saved in results/")
