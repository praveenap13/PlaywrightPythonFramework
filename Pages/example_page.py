from __future__ import annotations

from playwright.sync_api import expect

from Pages.base_page import BasePage


class ExamplePage(BasePage):
    """Page object for the public Playwright example page."""

    heading = "h1"

    def open(self, url: str) -> None:
        self.navigate(url)

    def verify_heading(self, text: str) -> None:
        expect(self.page.locator(self.heading)).to_have_text(text)
