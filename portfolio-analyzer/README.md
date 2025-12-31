# Portfolio Analyzer

Streamlit dashboard for exploring portfolio holdings, performance, and configuration data sourced from Alpha Vantage.

## Setup

1. Copy `.env.example` to `.env`, fill in real values, and add your Alpha Vantage API key under `API_TOKEN`.
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

Load values via `.env` (see `.env.example`). The app uses `PORTFOLIO_NAME`, `DATA_SOURCE`, `API_TOKEN`, and `LOG_LEVEL` (defaults to `INFO`) when present. Stock prices and history are pulled from the Alpha Vantage API documented at [https://www.alphavantage.co](https://www.alphavantage.co).
