from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverPath ="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"

driver = webdriver.Chrome(executable_path=driverPath)



# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# englishArticles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# englishArticles.click()



# allPortals = driver.find_element_by_link_text("All portals")
# allPortals.click()



# searchBar = driver.find_element_by_name("search")
# searchBar.send_keys("Python")
# searchBar.send_keys(Keys.ENTER)



driver.get("http://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element_by_xpath('/html/body/form/input[1]')
firstName.send_keys("Brent")

lastName = driver.find_element_by_xpath('/html/body/form/input[2]')
lastName.send_keys("Littlefield")

email = driver.find_element_by_xpath('/html/body/form/input[3]')
email.send_keys("bl@Little.ca")

submit = driver.find_element_by_xpath('/html/body/form/button')
submit.click()


driver.quit()
