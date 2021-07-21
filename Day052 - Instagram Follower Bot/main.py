from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

DRIVER_PATH = "YOUR CHROME DRIVER PATH"
ACCOUNT = "buzzfeedtasty"
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"


class InstaFollower:

    def __init__ (self, path):
        self.driver = webdriver.Chrome(executable_path = path)



    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)



    def findFollowers(self):
        time.sleep(5)
        
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)

        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        allButtons = self.driver.find_elements_by_css_selector("li button")
        for button in allButtons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancelButton = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancelButton.click()


bot = InstaFollower(DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()