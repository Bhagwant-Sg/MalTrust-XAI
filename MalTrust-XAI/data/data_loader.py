# data/data_loader.py
import os
import glob
from config.config import EXPERIMENT_CONFIG, WIN64_TRAIN_PATH, WIN64_TEST_PATH

def load_train_files():
    """Load training and test JSONL files."""
    train_files = sorted(glob.glob(os.path.join(WIN64_TRAIN_PATH, "*.jsonl")))
    test_files = sorted(glob.glob(os.path.join(WIN64_TEST_PATH, "*.jsonl")))

    active_count = EXPERIMENT_CONFIG["final_train_files"] if EXPERIMENT_CONFIG["run_mode"] == "final" else EXPERIMENT_CONFIG["debug_train_files"]

    print(f"Found {len(train_files)} train files. Using {active_count} files.")
    print(f"Found {len(test_files)} test files.")

    return train_files[:active_count], test_files