from playwright.sync_api import Page,expect

def test_sortwebtable(page:Page):
    page.goto("https://practice-automation.com/tables/")
    table=page.locator("table").nth(1)
    rows=table.locator("tr")
    expect(rows).to_have_count(11)
    expect(rows.first).to_be_visible()
    page.locator("text=Population (million)").click()
    # population_list=[]
    # for i in range(rows.count()):
    #     row=rows.nth(i)
    #     cells=row.locator("td")
    #     if cells.count() > 0:
    #         population=cells.nth(2).inner_text()
    #         population_list.append(population)
    # sorted_population_list=sorted(population_list,key=lambda x:float(x.replace(",","")))
    # assert population_list==sorted_population_list

    # for j in range(rows.count()):
    #     row=rows.nth(j)
    #     cells=row.locator("td")
    #     if cells.count() > 0 and cells.nth(0).inner_text() == "China":
    #         expect(cells.nth(1)).to_have_text("Asia")
    #         expect(cells.nth(2)).to_have_text("1,439")

    population_list1=[]
    print("Total rows in the table:",rows.count())
    for j in range(rows.count()):
        #cells= rows.nth(j).locator("td")   
        cells= rows.nth(1).locator("td")       
        population_text1 = cells.nth(2).inner_text()
        clean_value= population_text1.replace(",","")
        population1=float(clean_value)
        population_list1.append(population1)
    print("Population values",population_list1)

    







    