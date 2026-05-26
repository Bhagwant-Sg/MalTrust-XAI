# MalTrust-XAI - Additional Validity & Robustness Testing

**Q1 Revision Results for the Paper**  
*Temporal Validation, Robustness Stress Testing, External Validation (BODMAS), Deep Learning Baselines, McNemar Test & Calibration*

---

## Overview

This module contains all **additional validity experiments** for the MalTrust-XAI framework:

- Temporal (time-based) validation using EMBER2024 file dates
- Robustness testing (feature perturbation, packing proxy simulation)
- External validation on BODMAS dataset
- Deep learning baselines (MLP, Feature-CNN)
- Statistical tests (McNemar, Bootstrap CI)
- Calibration analysis

---

## How to Run

```bash
python main_validation.py --mode full# MalTrust-XAI Validation

Validation-oriented malware detection framework using:

- Leakage-aware preprocessing
- LightGBM malware detection
- SHAP explainability
- Temporal validation
- Robustness analysis
- Calibration analysis
- Cross-dataset validation
- Artifact integrity verification

## Repository Structure

- config/ : Experimental configuration
- data/ : Dataset loading utilities
- temporal/ : Temporal validation experiments
- robustness/ : Stress testing and perturbation analysis
- external/ : Cross-dataset evaluation
- deep/ : Lightweight neural baselines
- utils/ : Metrics and visualization utilities
- results/ : Experimental outputs
- notebooks/ : Original notebooks

## Dataset

Datasets are not redistributed.

Please obtain:

- EMBER2024
- BODMAS

from their official sources.
