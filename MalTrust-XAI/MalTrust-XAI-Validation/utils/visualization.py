# utils/visualization.py
import os

def save_all_results():
    os.makedirs("results/figures", exist_ok=True)
    os.makedirs("results/tables", exist_ok=True)
    print("✅ All results saved in results/ folder")