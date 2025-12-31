from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Holding:
    symbol: str
    shares: float
    price: float

    def value(self) -> float:
        return self.shares * self.price
