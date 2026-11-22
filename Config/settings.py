from __future__ import annotations

import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://www.saucedemo.com")
    browser: str = os.getenv("BROWSER", "chromium")
    headless: bool = os.getenv("HEADLESS", "false").lower() == "false"
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))
    default_timeout: float = float(os.getenv("DEFAULT_TIMEOUT", "10000"))

settings = Settings()
