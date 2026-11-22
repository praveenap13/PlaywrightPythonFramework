from playwright.sync_api import Page,expect

def test_webtable(page:Page):
    page.goto("https://practice-automation.com/tables/")
    table=page.locator("table").first
    rows=table.locator("tr")
    expect(rows).to_have_count(4)

    for i in range(rows.count()):
        row=rows.nth(i)
        cells=row.locator("td")
        for j in range(cells.count()):
            cell=cells.nth(j)
            print(f"Row {i+1}, Cell {j+1}: {cell.inner_text()}")

    for j in range(rows.count()):
               cell=rows.nth(j).locator("td")
               if cells.count() > 0 and cells.nth(0).inner_text() == "Oranges":
                   expect(cells.nth(1)).to_have_text("$3.99")
                   
                   
            


    