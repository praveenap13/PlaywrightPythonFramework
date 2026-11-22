from __future__ import annotations

import logging


def get_logger(name: str = "playwright-framework") -> logging.Logger:
    """Return a consistently configured logger for framework code."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        )
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
