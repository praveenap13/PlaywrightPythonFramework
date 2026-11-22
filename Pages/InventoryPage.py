from __future__ import annotations

from playwright.sync_api import expect

from Pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the SauceDemo inventory page."""

    URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_CONTAINER = "[data-test='inventory-container']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    SHOPPING_CART_LINK = "[data-test='shopping-cart-link']"
    SHOPPING_CART_BADGE = "[data-test='shopping-cart-badge']"

    def verify_inventory_page_is_visible(self) -> None:
        """Verify that the inventory page is displayed."""
        expect(self.page.locator(self.INVENTORY_CONTAINER)).to_be_visible()

    def add_product_to_cart(self, product_name: str) -> None:
        """Add a product to the cart by its visible name."""
        product = self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name)
        expect(product).to_have_count(1)
        product.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart(self, product_name: str) -> None:
        """Remove a product from the cart by its visible name."""
        product = self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name)
        expect(product).to_have_count(1)
        product.get_by_role("button", name="Remove").click()

    def add_backpack_to_cart(self) -> None:
        """Add the Sauce Labs Backpack to the cart."""
        self.add_product_to_cart("Sauce Labs Backpack")

    def add_bike_light_to_cart(self) -> None:
        """Add the Sauce Labs Bike Light to the cart."""
        self.add_product_to_cart("Sauce Labs Bike Light")

    def get_cart_item_count(self) -> int:
        """Return the number shown on the shopping cart badge."""
        if not self.is_visible(self.SHOPPING_CART_BADGE):
            return 0
        return int(self.get_text(self.SHOPPING_CART_BADGE))

    def open_cart(self) -> None:
        """Open the shopping cart."""
        self.click(self.SHOPPING_CART_LINK)
