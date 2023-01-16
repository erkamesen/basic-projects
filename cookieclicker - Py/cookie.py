from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys      # Enter Shift vb
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

# Pencere açılınca kapanmaması için driver options= parametresi ile yolluyoruz
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
###########################
# Deprecating hatası için pathi selenium.webdriver.chrome.service içinden Service classı ile yolluyoruz
s = Service(executable_path=chrome_driver_path)
##########################
driver = webdriver.Chrome(options=options ,service=s)


driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

# ZAMAN KISMI
timeout = time.time() + 4
five_min = time.time() + 60*30 #five minutes


cookieclicker = driver.find_element(By.ID, "cookie")
time.sleep(2)


while True:
    cookieclicker.click()


    if time.time() >= timeout:
        GRAYED = [j.text.replace(",", "").split("\n")[0] for j in driver.find_elements(By.CLASS_NAME, "grayed")]
        STORE = [i.text.replace(",", "") for i in driver.find_elements(By.CSS_SELECTOR, "#store div b")
                 if i.text.replace(",", "") not in GRAYED]

        money = 0
        name = ""
        for i in range(len(STORE)):
            if int(STORE[i].split("-")[-1]) > money:
                money = int(STORE[i].split("-")[-1])
                name = STORE[i].split("-")[0].strip()
        driver.find_element(By.ID, f"buy{name}").click()
        timeout = time.time() +5

        if time.time() >= five_min:
            print(driver.find_element(By.ID, "cps").text)
            driver.close()
            break



