from selenium import webdriver

driverPath ="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"

driver = webdriver.Chrome(executable_path=driverPath)



# driver.get("https://www.amazon.ca/Instant-Pot-Ultra-Electric-Stainless/dp/B06Y1MP2PY/ref=sr_1_3?crid=2U4F9TCKZI3BK&dchild=1&keywords=instant+pot&qid=1626564177&sprefix=instant%2Caps%2C285&sr=8-3")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)



# driver.get("https://www.python.org/")
# searchBar = driver.find_element_by_name("q")
# print(searchBar.tag_name)
# print(searchBar.get_attribute("placeholder"))



# driver.get("https://www.python.org/")
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)



# driver.get("https://www.python.org/")
# docLink = driver.find_element_by_css_selector(".documentation-widget a")
# print(docLink.text)



# driver.get("https://www.python.org/")
# bugLink = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bugLink.text)



driver.get("https://www.python.org/")

eventDates = driver.find_elements_by_css_selector(".event-widget time")
eventYears = driver.find_elements_by_css_selector(".event-widget time .say-no-more")
eventNames = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(eventDates)):
    events[n]={
        "time": f"{eventYears[n].get_attribute('innerHTML')}{eventDates[n].text}",
        "name": eventNames[n].text,
    }

print(events)


driver.quit()