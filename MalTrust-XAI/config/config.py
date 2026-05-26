# config/config.py
import os

BASE_PATH = "/kaggle/input/datasets/weiweip/ember2024"
WIN64_TRAIN_PATH = os.path.join(BASE_PATH, "Win64_train")
WIN64_TEST_PATH = os.path.join(BASE_PATH, "Win64_test")

EXPERIMENT_CONFIG = {
    "framework_name": "MalTrust-XAI",
    "dataset": "EMBER2024 Win64",
    "task": "Binary Malware Detection",
    "label_mapping": {0: "Benign", 1: "Malware"},

    "debug_train_files": 5,
    "final_train_files": 25,
    "run_mode": "final",

    "test_size": 0.15,
    "validation_size": 0.15,
    "random_state": 42,
    "final_selected_feature_count": 256,
}