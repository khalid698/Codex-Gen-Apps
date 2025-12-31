from __future__ import annotations

import logging
import time
from typing import Iterable

import httpx

from src.models.portfolio import Holding
from src.utils.config import get_app_config
from src.utils.logging import configure_logging

configure_logging()

ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
DEFAULT_HOLDINGS = [
    
    {"symbol": "MSFT", "shares": 15.0, "fallback_price": 315.10},
    {"symbol": "AAPL", "shares": 25.0, "fallback_price": 174.20},
    {"symbol": "GOOGL", "shares": 8.0, "fallback_price": 136.45},
    {"symbol": "VNQ", "shares": 40.0, "fallback_price": 105.23},
]
LOGGER = logging.getLogger(__name__)


def _fetch_global_quote(symbol: str, api_key: str, client: httpx.Client) -> dict[str, str] | None:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key,
    }
    try:
        response = client.get(ALPHA_VANTAGE_URL, params=params, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return data.get("Global Quote")
    except (httpx.HTTPError, ValueError) as exc:
        LOGGER.warning("Failed to fetch quote for %s: %s", symbol, exc)
        return None


def _fetch_monthly_series(symbol: str, api_key: str, client: httpx.Client) -> dict[str, dict[str, str]] | None:
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol,
        "apikey": api_key,
    }
    try:
        response = client.get(ALPHA_VANTAGE_URL, params=params, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return data.get("Monthly Time Series")
    except (httpx.HTTPError, ValueError) as exc:
        LOGGER.warning("Failed to fetch monthly series for %s: %s", symbol, exc)
        return None


def get_holdings() -> Iterable[Holding]:
    config = get_app_config()
    LOGGER.debug("API_Token: %s", config.api_token)
    if not config.api_token:
        return _fallback_holdings()

    holdings: list[Holding] = []
    with httpx.Client() as client:
        for item in DEFAULT_HOLDINGS:
            quote = _fetch_global_quote(item["symbol"], config.api_token, client)
            price = item["fallback_price"]
            if quote:
                price = float(quote.get("05. price", price))
            holdings.append(Holding(symbol=item["symbol"], shares=item["shares"], price=price))
            time.sleep(15)
    return holdings


def get_performance() -> dict[str, float]:
    config = get_app_config()
    if not config.api_token:
        return _fallback_performance()

    with httpx.Client() as client:
        quote = _fetch_global_quote(DEFAULT_HOLDINGS[0]["symbol"], config.api_token, client)
        if not quote:
            return _fallback_performance()
        change_percent = quote.get("10. change percent", "0.0%").strip("%")
        metric = float(change_percent or "0.0")
        return {
            "1W": metric,
            "1M": metric * 1.5,
            "3M": metric * 2.0,
            "YTD": metric * 3.5,
        }


def get_performance_history() -> list[dict[str, float]]:
    config = get_app_config()
    if not config.api_token:
        return _fallback_history()

    with httpx.Client() as client:
        series = _fetch_monthly_series(DEFAULT_HOLDINGS[0]["symbol"], config.api_token, client)
        if not series:
            return _fallback_history()

        dates = sorted(series.keys())[-5:]
        history = []
        for date in dates:
            month_data = series[date]
            close = float(month_data.get("4. close", "0") or "0")
            prev_date = dates[max(dates.index(date) - 1, 0)]
            prev_close = float(series[prev_date].get("4. close", "0") or "0")
            change = ((close - prev_close) / prev_close * 100) if prev_close else 0.0
            history.append({"date": date, "return": round(change, 2)})
        return history


def _fallback_holdings() -> list[Holding]:
    return [
        Holding(symbol=item["symbol"], shares=item["shares"], price=item["fallback_price"])
        for item in DEFAULT_HOLDINGS
    ]


def _fallback_performance() -> dict[str, float]:
    return {"1W": 1.8, "1M": 4.3, "3M": 6.9, "YTD": 12.4}


def _fallback_history() -> list[dict[str, float]]:
    return [
        {"date": "2024-01-01", "return": 0.4},
        {"date": "2024-02-01", "return": 1.1},
        {"date": "2024-03-01", "return": -0.3},
        {"date": "2024-04-01", "return": 2.2},
        {"date": "2024-05-01", "return": 1.7},
    ]
