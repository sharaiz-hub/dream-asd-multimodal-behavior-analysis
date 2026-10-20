# Technical audit of supplied ASD.zip

## Confirmed contents
- 61 archive entries prior to packaging, including 21 PNG figures, 11 CSV results and 1 EDA JSON summary.
- `configs/config.yaml` contains a CAMGT model configuration and LOSO settings.
- `src/utils.py` implements config loading, seeding, device selection, logging, result saving and parameter counting.
- `src/models/`, `src/training/`, `src/dataset/`, `src/evaluation/`, and `src/explainability/` contain only `__init__.py` scaffolding.
- No dataset, model definitions, checkpoints, or training/evaluation entry points in supplied archive.

## Critical caveats
- No reproduction of model training or metrics is possible from these files alone.
- Historical CSV outputs do not establish their training run, fold definitions, provenance or absence of leakage.
- EDA summary includes anomalous task categories such as numeric strings; data-cleaning assumptions need inspection.
- The configuration has three severity classes (`NS`, `ASD`, `AUT`) but some result CSVs use binary labels. The mapping requires explicit documentation.
- Subject-level behavioral and ADOS data are potentially sensitive; excluded subject-identified CSVs from this upload package.
- Data URL supplied by user was not retrievable through the connected Google Drive integration; availability unverified.

## Audit scope
Static archive inspection and packaging only. No dataset access, model execution, result replication or license verification.
