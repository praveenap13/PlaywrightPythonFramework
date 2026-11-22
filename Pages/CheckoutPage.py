from __future__ import annotations

from playwright.sync_api import expect

from Pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the SauceDemo cart and checkout flow."""

    CART_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-one.html"
    COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

    CHECKOUT_BUTTON = "[data-test='checkout']"
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    FINISH_BUTTON = "[data-test='finish']"
    CANCEL_BUTTON = "[data-test='cancel']"
    ERROR_MESSAGE = "[data-test='error']"
    COMPLETE_HEADER = "[data-test='complete-header']"

    def open_cart(self) -> None:
        """Open the SauceDemo shopping cart."""
        self.navigate(self.CART_URL)

    def click_checkout(self) -> None:
        """Start checkout from the shopping cart."""
        self.click(self.CHECKOUT_BUTTON)

    def enter_first_name(self, first_name: str) -> None:
        """Enter the customer's first name."""
        self.fill(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Enter the customer's last name."""
        self.fill(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Enter the customer's postal code."""
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def enter_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """Fill in all required customer information."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def continue_to_overview(self) -> None:
        """Continue from customer information to the order overview."""
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self) -> None:
        """Submit the order from the overview page."""
        self.click(self.FINISH_BUTTON)

    def cancel_checkout(self) -> None:
        """Cancel checkout and return to the previous page."""
        self.click(self.CANCEL_BUTTON)

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Complete customer information and continue to order overview."""
        self.enter_customer_information(first_name, last_name, postal_code)
        self.continue_to_overview()

    def verify_checkout_error(self, message: str) -> None:
        """Verify that checkout displays the expected validation error."""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(message)

    def verify_order_complete(self, message: str = "Thank you for your order!") -> None:
        """Verify that the order confirmation is displayed."""
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text(message)
