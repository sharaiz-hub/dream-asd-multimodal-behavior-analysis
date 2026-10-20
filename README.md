# DREAM Autism Research: Multimodal Behavioral Modeling and Experimental Results

**implementation:** Sharaiz Shahid  

**Use:** Research and educational evaluation only. Not a clinical diagnostic tool.

## Overview

This repository documents experiments associated with the DREAM autism research dataset, including subject-level behavioral modeling, sequence-learning experiments, ablations, and saved visualizations. The supplied archive contains a project configuration, a utility module, historical results and figures. **The actual model, dataset loader, training, and evaluation implementations are not included in the supplied archive.** Accordingly, it would be inaccurate to claim this repository presently supports training or independently reproducing the reported metrics.

## Research question

Can time-varying behavioral signals, including skeletal motion, head gaze and eye gaze, support subject-level modeling of autism-related behavioral assessments? The configuration indicates exploration of attention-based multimodal modeling and subject-wise evaluation; it does **not** independently establish that those experiments ran as configured.

## Dataset

The provided `configs/config.yaml` describes 61 subjects, 3,121 sessions in the saved EDA summary, modalities `skeleton`, `head_gaze`, and `eye_gaze`, and tasks TT, IM and JA. These are historical project records, not newly validated counts. The raw dataset is **not bundled**.

Dataset reference supplied by the maintainer: [Google Drive file](https://drive.google.com/file/d/1GRCPSlK6Gr_iqhE3eQKlTgwMJmS_Gc8a/view?usp=share_link). **Access, ownership and redistribution rights have not been verified.** Obtain data only through an authorized channel; do not publish participant data or access-controlled copies.

## Methodology represented by configuration

- 128-frame windows, 64-frame training stride and 128-frame test stride
- Per-subject normalization and confidence-based filtering specified in YAML
- Configured model `CAMGT`: `d_model=64`, 4 attention heads, 3 layers
- Configured 61-fold leave-one-subject-out validation
- Listed metrics: MAE, RMSE, ICC, ECE, macro-F1, confusion matrix

**Important:** These are configuration values. The missing training scripts prevent confirmation that each setting was applied to the historical experiments. Files with `lstm`, `ensemble`, and `ablation` in their names are historical artifacts, not executable proof of an implementation.

## Results and figures

See [Results and evidence](docs/RESULTS.md) and [Figure index](docs/FIGURES.md). The saved CSVs and plots represent **historical outputs only**, not independently reproduced performance. Some subject-level CSVs were intentionally excluded from this upload package because they include subject identifiers and behavioral/assessment-related fields.

## Repository structure

```text
configs/config.yaml            Experiment configuration
src/utils.py                  Shared utility functions (only substantive Python source in archive)
src/{models,training,...}/    Empty package scaffolding; implementations not included
experiments/figures/          Historical figures
experiments/results/          Historical result files without selected subject-level records
docs/                         Methods, results, figure index, provenance and reproduction status
tests/                        Empty test package scaffolding
```

## Installation and execution status

This is **not** a runnable end-to-end pipeline. To inspect the utility module in a local Python environment:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m compileall -q src
```

No valid `train.py` or inference command can be supplied until the missing implementations are recovered. Do not mistake a successful syntax check for a model validation.

## Maintainer contributions: Sharaiz Shahid

- Provided and organized this research archive for repository documentation.
- Repository packaging and evidence-status documentation for the current version.
- Historical experiments are associated with the maintainer's project, but **individual model development and experiment execution cannot be independently verified from the supplied files alone**.

## Limitations and next steps

1. Restore model definitions, dataset loaders, training scripts, evaluation scripts and checkpoints with provenance.
2. Audit subject-wise splits and any ADOS-derived decision rules to exclude target leakage.
3. Validate all results using a held-out, subject-independent protocol and report uncertainty.
4. Review dataset licensing, participant privacy, consent and distribution permissions.
5. Add a reproducible environment lockfile and automated smoke tests.

See [Technical audit](docs/TECHNICAL_AUDIT.md) for the evidence boundary. No claim of clinical utility or generalizability is made.

## License and release policy

No code license has been assigned because the ownership and licensing status of all constituent materials have not been established. **Private repository use does not itself grant rights to upload restricted data or third-party code.** Verify permissions before sharing or publishing.
