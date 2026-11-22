from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page
from playwright.sync_api import expect


class BasePage:
    """Reusable synchronous Playwright actions for page objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str, wait_until: str = "domcontentloaded") -> None:
        self.page.goto(url, wait_until=wait_until)  # type: ignore[arg-type]

    def go_back(self) -> None:
        self.page.go_back(wait_until="domcontentloaded")

    def reload(self) -> None:
        self.page.reload(wait_until="domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def click(self, selector: str, **kwargs: object) -> None:
        self.page.locator(selector).click(**kwargs)

    def fill(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    def clear(self, selector: str) -> None:
        self.page.locator(selector).clear()

    def press(self, selector: str, key: str) -> None:
        self.page.locator(selector).press(key)

    def select_option(self, selector: str, value: str) -> None:
        self.page.locator(selector).select_option(value)

    def check(self, selector: str) -> None:
        self.page.locator(selector).check()

    def uncheck(self, selector: str) -> None:
        self.page.locator(selector).uncheck()

    def hover(self, selector: str) -> None:
        self.page.locator(selector).hover()

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_for_visible(self, selector: str) -> None:
        expect(self.page.locator(selector)).to_be_visible()

    def wait_for_text(self, selector: str, text: str) -> None:
        expect(self.page.locator(selector)).to_contain_text(text)

    def wait_for_url(self, url: str) -> None:
        self.page.wait_for_url(url)

    def take_screenshot(self, path: str | Path, full_page: bool = True) -> None:
        screenshot_path = str(path)
        Path(screenshot_path).parent.mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=screenshot_path, full_page=full_page)

















































