from __future__ import annotations

import logging

from src.utils.config import get_app_config


def configure_logging() -> None:
    config = get_app_config()
    level = getattr(logging, config.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
