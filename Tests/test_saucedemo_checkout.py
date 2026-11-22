from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

from Pages.CheckoutPage import CheckoutPage
from Pages.InventoryPage import InventoryPage
from Pages.LoginPage import LoginPage


@pytest.mark.smoke
def test_user_can_complete_saucedemo_checkout(page: Page) -> None:
    """Verify that a user can add a product and complete an order."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url(InventoryPage.URL)
    inventory_page.verify_inventory_page_is_visible()

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_item_count() == 1
    inventory_page.open_cart()
    expect(page).to_have_url(CheckoutPage.CART_URL)

    checkout_page.click_checkout()
    expect(page).to_have_url(CheckoutPage.CHECKOUT_URL)
    checkout_page.checkout("Praveena", "Tester", "12345")
    checkout_page.finish_order()

    expect(page).to_have_url(CheckoutPage.COMPLETE_URL)
    checkout_page.verify_order_complete()
