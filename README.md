# Investment Portfolio Analyzer

## Setup

- Install dependencies (Python 3.11+ recommended):
  ```bash
  pip install .
  # or, for editable installs:
  pip install -e .
  ```
- Copy `.env.example` to `.env` and fill in secrets before running.

## Running

- Start the Streamlit dashboard:
  ```bash
  make run
  ```
  Navigate through the sidebar to see Overview, Holdings, Performance, and Settings placeholders.

## Lint & Test

- `make lint`
- `make test`

## Project Layout

- `app.py` – Streamlit entrypoint that orchestrates navigation and page rendering.
- `src/ui/` – UI helpers and page definitions.
- `src/services/` – Data-fetching or simulation helpers.
- `src/models/` – Domain models representing holdings and performance summaries.
- `src/utils/` – Infrastructure helpers (environment config, helpers).
