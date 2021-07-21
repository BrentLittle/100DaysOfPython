from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver")
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        runTestBtn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        runTestBtn.click()

        time.sleep(60)

        downloadSpeed = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        uploadSpeed = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

        print(f"Download: {downloadSpeed.text}")
        print(f"upload: {uploadSpeed.text}")


bot = InternetSpeedBot()

bot.get_internet_speed()