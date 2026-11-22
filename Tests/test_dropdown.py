import asyncio 
from playwright.async_api import async_playwright

async def test_dropdown():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://practice-automation.com/form-fields/")
        dropdown = page.locator("#automation")
        await dropdown.scroll_into_view_if_needed()
        assert await dropdown.is_visible()
        options = dropdown.locator("option")
        dropdown_count = await options.count()
        #assert dropdown_count == 4
        assert await options.count() == 4
        default_selected=await dropdown.evaluate(
         "el  => el.options[el.selectedIndex].text"
        )
        print("Default selected option is:", default_selected)
        expected_data = [
            ("default", ""),
            ("yes", "Yes"),
            ("no", "No"),
            ("undecided", "Undecided")
        ]

        for i in range(len(expected_data)):
            assert await options.nth(i).get_attribute("value") == expected_data[i][0]

        await browser.close()














        