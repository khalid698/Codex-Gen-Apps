from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(".env")


@dataclass(frozen=True)
class AppConfig:
    portfolio_name: str
    data_source: str
    api_token: str | None


def _ensure_env_loaded() -> None:
    load_dotenv(dotenv_path=ENV_PATH, override=False)


def get_app_config() -> AppConfig:
    _ensure_env_loaded()
    return AppConfig(
        portfolio_name=os.getenv("PORTFOLIO_NAME", "Portfolio Analyzer"),
        data_source=os.getenv("DATA_SOURCE", "simulated"),
        api_token=os.getenv("API_TOKEN") or None,
    )
