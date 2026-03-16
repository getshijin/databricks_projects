# Databricks & Snowflake Practice Repository

This repository contains learning and experimentation material for two data platforms:

- **Databricks**: notebooks, scripts, and sample datasets focused on Delta Lake, Auto Loader, and related workflows.
- **Snowflake**: SQL examples and topic-based folders (loading data, streams, tasks, time travel, zero copy, and more).

## Repository layout

- `Databricks/`
  - `Notebook/`: Databricks-oriented Python notebooks/scripts.
  - `dataset/`: sample input data for notebook exercises.
- `Snowflake/`
  - Topic folders with SQL scripts and notes for specific Snowflake features.
- `import kagglehub.py`
  - Helper script for importing dataset assets with `kagglehub`.

## How to use

1. Open the platform-specific folder (`Databricks` or `Snowflake`).
2. Run notebooks/scripts in your Databricks workspace, or execute SQL files in Snowflake.
3. Adjust paths, credentials, and warehouse/cluster settings to match your environment.

## Notes

- Some files are generated or bundled dependencies used by local notebook experiments.
- This repo is intended as a reference/practice workspace rather than a packaged application.
