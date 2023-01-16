from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys      # Enter Shift vb
import time
from infosfordataautomation import FORMURL




class Dataenter:
    def __init__(self):
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.URL = FORMURL
        # Pencere açılınca kapanmaması için driver options= parametresi ile yolluyoruz
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        ###########################
        # Deprecating hatası için pathi selenium.webdriver.chrome.service içinden Service classı ile yolluyoruz
        s = Service(executable_path=chrome_driver_path)
        ##########################
        self.driver = webdriver.Chrome(options=options ,service=s)


    def openPage(self):
        self.driver.get(url=self.URL)
        self.driver.maximize_window()

    def inputPart(self , link, price, address):
        self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                      '/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            link, Keys.TAB, price, Keys.TAB, address,Keys.TAB, Keys.ENTER
        )
        time.sleep(3)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    def closePage(self):
        self.driver.close()


