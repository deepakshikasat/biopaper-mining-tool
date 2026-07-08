# BioPaper Mining Tool

Literature mining upgraded from three demo rows to **real PubMed abstracts fetched through NCBI E-utilities**. Extraction is intentionally lightweight and rule-based so the workflow runs without an LLM API key; the schema is ready for Claude/LLM extraction when credentials are available.

## Reproduce

```bash
python scripts/run_pipeline.py
```

## Outputs

- `outputs/extracted_abstracts.csv`
- `outputs/mechanism_keyword_counts.csv`
- `figures/modality_counts.svg`
- `src/pubmed.py`
- `app.py`

## Analysis Report

Open `reports/analysis_report.html` for the hypothesis, public data provenance, process, outputs, and interpretation.

## Portfolio Note

This repository uses public data sources or clearly labelled synthetic demonstration data only. No employer-owned or confidential data are included.
