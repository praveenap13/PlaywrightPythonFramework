from __future__ import annotations

from playwright.sync_api import expect

from Pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the SauceDemo login page."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self) -> None:
        """Open the SauceDemo login page."""
        self.navigate(self.URL)

    def enter_username(self, username: str) -> None:
        """Enter a username into the login form."""
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        """Enter a password into the login form."""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        """Submit the login form."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Log in with the supplied SauceDemo credentials."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_error(self, message: str) -> None:
        """Verify that the login form displays the expected error."""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(message)

    def is_login_error_visible(self) -> bool:
        """Return whether the login error message is visible."""
        return self.is_visible(self.ERROR_MESSAGE)
