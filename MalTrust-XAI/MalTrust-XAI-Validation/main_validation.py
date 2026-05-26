# main_validation.py
import argparse
from config.config import CONFIG
from data.chunk_loader import load_or_create_chunks
from temporal.temporal_validation import run_temporal_validation
from robustness.stress_testing import run_robustness_tests
from external.bodmas_validation import run_external_validation
from deep.deep_baselines import run_deep_baselines
from stats.statistical_tests import run_statistical_tests
from utils.visualization import save_all_results

def main():
    parser = argparse.ArgumentParser(description="MalTrust-XAI Validation Module")
    parser.add_argument('--mode', type=str, default='full',
                        choices=['full', 'temporal', 'robustness', 'external', 'deep', 'stats'])
    args = parser.parse_args()

    print(f" Running Validation Mode: {args.mode.upper()}")

    # Load numeric chunks
    chunk_paths, label_col = load_or_create_chunks()

    if args.mode in ['full', 'temporal']:
        temporal_results = run_temporal_validation(chunk_paths, label_col)

    if args.mode in ['full', 'robustness']:
        robustness_results = run_robustness_tests()

    if args.mode in ['full', 'external']:
        external_results = run_external_validation()

    if args.mode in ['full', 'deep']:
        deep_results = run_deep_baselines()

    if args.mode in ['full', 'stats']:
        stats_results = run_statistical_tests()

    # Save everything
    save_all_results()

    print(" All validation experiments completed successfully!")

if __name__ == "__main__":
    main()