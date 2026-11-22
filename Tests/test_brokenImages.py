from playwright.sync_api import Page,expect

def test_brkokenImg(page:Page):
    page.goto("https://practice-automation.com/broken-images/")
