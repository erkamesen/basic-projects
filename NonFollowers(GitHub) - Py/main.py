from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # Enter Shift bla bla
import time
from github import Follow
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME") # replace with your github username
PASSWORD = os.getenv("PASSWORD") # replace with your github password

tracker = Follow(USERNAME) #github username
traitors_list = tracker.non_followers()

driver_path = "./geckodriver" # replace with your browser driver s path

options = webdriver.FirefoxOptions() # ChromeOptions for chrome
s = Service(executable_path=driver_path)

##########################
driver = webdriver.Firefox(options=options, service=s)


driver.get("http://www.github.com")


# Login

login = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
login.click()

time.sleep(1)
login = driver.find_element(By.ID, "login_field").send_keys(USERNAME,
                                                            Keys.TAB,
                                                            PASSWORD,
                                                            Keys.TAB,
                                                            Keys.ENTER)


time.sleep(1)



for traitor in traitors_list:
    driver.get(f"http://www.github.com/{traitor}")
    time.sleep(1)
    kill_him = driver.find_element(By.CSS_SELECTOR, "span.user-following-container:nth-child(3) > form:nth-child(2) > input:nth-child(2)")
    kill_him.click()
    time.sleep(1.5)
    



