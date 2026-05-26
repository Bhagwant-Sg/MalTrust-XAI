# main.py
import argparse
from config.config import EXPERIMENT_CONFIG
from data.data_loader import load_train_files
from models.train import train_baseline_models
from utils.visualization import save_final_visualizations

def main():
    parser = argparse.ArgumentParser(description="MalTrust-XAI Malware Detection Framework")
    parser.add_argument('--mode', type=str, default='final', choices=['debug', 'final'],
                        help='Run mode: debug or final')
    args = parser.parse_args()

    EXPERIMENT_CONFIG["run_mode"] = args.mode
    print(f"🚀 Starting MalTrust-XAI in {args.mode.upper()} mode...")

    # Step 1: Load Data
    train_files, test_files = load_train_files()

    # Step 2: Train Models
    results = train_baseline_models(train_files)

    # Step 3: Generate Visualizations & Reports
    save_final_visualizations(results)

    print("✅ MalTrust-XAI Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()