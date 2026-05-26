# data/chunk_loader.py
import os, glob, json, gc, random
import pandas as pd
import numpy as np
from tqdm import tqdm
from config.config import CONFIG

def flatten_numeric_only(obj, parent_key="", sep="_"):
    out = {}
    for k, v in obj.items():
        key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            out.update(flatten_numeric_only(v, key, sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, (int, float, bool, np.integer, np.floating)):
                    out[f"{key}_{i}"] = item
        else:
            if isinstance(v, (int, float, bool, np.integer, np.floating)):
                out[key] = v
    return out

def load_or_create_chunks():
    chunk_dir = CONFIG["WORK_DIR"]
    os.makedirs(chunk_dir, exist_ok=True)
    
    files = sorted(glob.glob(CONFIG["DATA_ROOT"] + "/**/*.jsonl", recursive=True))
    chunk_paths = []
    
    for i, fp in enumerate(tqdm(files[:30])):  # Limit for safety
        selected = []
        with open(fp, "r", errors="ignore") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    flat = flatten_numeric_only(obj)
                    if "label" in flat:
                        selected.append(flat)
                except:
                    continue
                if len(selected) >= CONFIG["ROWS_PER_FILE"]:
                    break
        
        if selected:
            df = pd.DataFrame(selected)
            df = df.fillna(0).astype(np.float32)
            path = os.path.join(chunk_dir, f"chunk_{i:03d}.parquet")
            df.to_parquet(path, index=False)
            chunk_paths.append(path)
    
    return chunk_paths, "label"