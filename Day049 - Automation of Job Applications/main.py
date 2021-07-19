from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNTEMAIL = ""
ACCOUNTPASSWORD = ""


driverPath ="C:\\Users\\Brent\\Desktop\\Webdrivers\\chromedriver"
driver = webdriver.Chrome(executable_path=driverPath)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&sortBy=R")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(2)

emailInput = driver.find_element_by_id("username")
emailInput.send_keys(ACCOUNTEMAIL)

passwordInput = driver.find_element_by_id("password")
passwordInput.send_keys(ACCOUNTPASSWORD)

passwordInput.send_keys(Keys.ENTER)

time.sleep(3)
jobs = driver.find_elements_by_css_selector(".jobs-search-results__list .job-card-list__title")

jobsAndLinks = {}

for n in range(len(jobs)):
    jobsAndLinks[n] = {
        "Job Title": jobs[n].text,
        "Link": jobs[n].get_attribute("href"),
    }

print(jobsAndLinks)
