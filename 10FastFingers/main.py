from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # Enter Shift bla bla
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time



driver_path = "./geckodriver"  # replace with your browser driver s path
options = webdriver.FirefoxOptions()  # Its Firefox if u use chrome set ChromeOptions for chrome


s = Service(executable_path=driver_path)
##########################
driver = webdriver.Firefox(options=options, service=s)

URL = "https://10fastfingers.com/typing-test/english"

driver.get(URL)
time.sleep(2)


driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
driver.maximize_window()
time.sleep(2)


inputfield = driver.find_element(By.ID, "inputfield")


while True:
    word = driver.find_element(By.CLASS_NAME, "highlight").text.strip()

    inputfield.send_keys(word, Keys.ENTER, Keys.SPACE)
    time.sleep(0.1)