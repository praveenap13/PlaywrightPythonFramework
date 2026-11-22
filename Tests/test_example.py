from __future__ import annotations

import json
from pathlib import Path

import pytest
from playwright.sync_api import Page

from Config.settings import settings
from Pages.example_page import ExamplePage


TEST_DATA = json.loads(
    (Path(__file__).parents[1] / "Testdata" / "test_data.json").read_text(encoding="utf-8")
)


@pytest.mark.smoke
def test_playwright_homepage(page: Page) -> None:
    example_page = ExamplePage(page)
    example_page.open(settings.base_url)
    example_page.verify_heading(TEST_DATA["example_page"]["heading"])
