from selenium import webdriver
import time


driverPath ="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"
driver = webdriver.Chrome(executable_path=driverPath)



driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

itemIds = [item.get_attribute("id") for item in driver.find_elements_by_css_selector("#store div")]

timeout = time.time() + 2

while True:
    cookie.click()

    if time.time() >timeout:
        
        #Get all upgrade price tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        
        #Convert upgrade tag to an integer price.
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = itemIds[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        

        timeout = time.time() + 2


