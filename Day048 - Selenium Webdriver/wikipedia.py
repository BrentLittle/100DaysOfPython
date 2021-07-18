from selenium import webdriver

driverPath ="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"

driver = webdriver.Chrome(executable_path=driverPath)



driver.get("https://en.wikipedia.org/wiki/Main_Page")
englishArticles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(englishArticles.text)



driver.quit()