from __future__ import annotations

from typing import Iterable

from src.models.portfolio import Holding


def get_holdings() -> Iterable[Holding]:
    return [
        Holding(symbol="AAPL", shares=25.0, price=174.20),
        Holding(symbol="MSFT", shares=15.0, price=315.10),
        Holding(symbol="GOOGL", shares=8.0, price=136.45),
        Holding(symbol="VNQ", shares=40.0, price=105.23),
    ]


def get_performance() -> dict[str, float]:
    return {"1W": 1.8, "1M": 4.3, "3M": 6.9, "YTD": 12.4}


def get_performance_history() -> list[dict[str, float]]:
    return [
        {"date": "2024-01-01", "return": 0.4},
        {"date": "2024-02-01", "return": 1.1},
        {"date": "2024-03-01", "return": -0.3},
        {"date": "2024-04-01", "return": 2.2},
        {"date": "2024-05-01", "return": 1.7},
    ]
