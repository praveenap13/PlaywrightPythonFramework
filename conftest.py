from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from Config.settings import settings


REPORTS_DIR = Path(__file__).parent / "Reports"


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser(
    playwright: Playwright,
    request: pytest.FixtureRequest,
) -> Generator[Browser, None, None]:
    """Launch one configured browser for the test session."""
    browser_type = getattr(playwright, settings.browser)
    headed = bool(request.config.getoption("--headed", default=False))
    launched_browser = browser_type.launch(
        headless=settings.headless and not headed,
        slow_mo=settings.slow_mo,
    )
    yield launched_browser
    launched_browser.close()


@pytest.fixture
def context(browser: Browser, request: pytest.FixtureRequest) -> Generator[BrowserContext, None, None]:
    """Create an isolated browser context for each test."""
    test_name = request.node.name
    video_option = request.config.getoption("--video", default=None)
    record_video = video_option not in (None, False, "off")
    test_context = browser.new_context(
        base_url=settings.base_url,
        record_video_dir=str(REPORTS_DIR / "videos") if record_video else None,
    )
    test_context.set_default_timeout(settings.default_timeout)
    test_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield test_context
    trace_path = REPORTS_DIR / "traces" / f"{test_name}.zip"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    test_context.tracing.stop(path=str(trace_path))
    test_context.close()


@pytest.fixture
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    """Create a fresh page for each test and capture failures."""
    test_page = context.new_page()
    yield test_page
    test_report = getattr(request.node, "rep_call", None)
    if test_report is not None and test_report.failed:
        screenshot_path = REPORTS_DIR / "screenshots" / f"{request.node.name}.png"
        screenshot_path.parent.mkdir(parents=True, exist_ok=True)
        test_page.screenshot(path=str(screenshot_path), full_page=True)
    test_page.close()


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "smoke: fast critical-path checks")
    config.addinivalue_line("markers", "regression: broader functional coverage")


def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]) -> None:
    if "page" in item.fixturenames:
        report = pytest.TestReport.from_item_and_call(item, call)
        setattr(item, f"rep_{report.when}", report)
