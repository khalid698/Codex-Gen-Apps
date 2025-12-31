# Portfolio Analyzer

Streamlit dashboard for exploring portfolio holdings, performance, and configuration data.

## Setup

1. Copy `.env.example` to `.env` and fill in real values if needed.
2. Create and activate a Python 3.11+ virtual environment.
3. Install the package:
   ```sh
   python -m pip install -e .[dev]
   ```

## Development commands

| Command | Purpose |
| --- | --- |
| `make run` | Start Streamlit app (`streamlit run app.py`). |
| `make lint` | Run `ruff` across `src` and `tests`. |
| `make test` | Run `pytest`. |

## Environment Variables

Load values via `.env` (see `.env.example`). The app uses `PORTFOLIO_NAME`, `DATA_SOURCE`, and `API_TOKEN` when present.
