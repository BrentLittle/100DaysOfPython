from bs4 import BeautifulSoup
from selenium import webdriver
import requests, time

CHROME_DRIVER = "C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"

GOOGLE_FORM = "https://forms.gle/t61bDuf1cn2K7UVt9"

ZILLOW = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-76.76131547480048%2C%22east%22%3A-76.28341020136298%2C%22south%22%3A44.07754027894915%2C%22north%22%3A44.42232287618241%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A1235192%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%7D%7D"

BROWSER_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=options)


response = requests.get(url=ZILLOW, headers=BROWSER_HEADER)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")


links = soup.find_all(name="a", class_="list-card-img")
for n in range(len(links)):
    linkText = links[n].get("href")
    if ("https" not in linkText) :
        links[n] = f"https://www.zillow.com{linkText}"
    else:
        links[n] = linkText


prices = soup.find_all(name="div", class_="list-card-price")
for n in range(len(prices)):
    prices[n] = prices[n].getText().split("/")[0].split(" ")[0].replace("+","").replace("C","")


addresses = soup.find_all(name="address", class_="list-card-addr")
for n in range(len(addresses)):
    addresses[n] = addresses[n].getText()


for n in range(len(links)):
    driver.get(GOOGLE_FORM)
    time.sleep(1)
        
    addressBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        
    priceBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    URLBox =  driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submitBtn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    
    addressBox.send_keys(addresses[n])
    priceBox.send_keys(prices[n])
    URLBox.send_keys(links[n])
    submitBtn.click()

    time.sleep(0.5)

driver.quit()








