from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Twitter:

    def __init__(self, ID, password, msg):
        self.msg = msg
        self.ID = ID
        self.password = password
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        s = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(options=options, service=s)
        self.URL = "https://www.twitter.com/"

    def openTw(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def loginPart(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div'
                                           '/div[2]/div[2]/div/div/div[1]/a/div/span/span').click()
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div'
                      '/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(
            self.ID, Keys.ENTER
        )

        time.sleep(2)

        gvkullanici = self.driver.find_element(By.CSS_SELECTOR,
                                 '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')


        gvkullanici.send_keys(
                "erkam_esen", Keys.ENTER
            )
        time.sleep(2)
        sifregiris = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        sifregiris.send_keys(
            self.password, Keys.ENTER)

    def tweet(self):
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]'
                                           '/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label'
                                           '/div[1]/div/div/div/div/div/div[2]/div').send_keys(
            self.msg
        )
        time.sleep(4)

        self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]'
                      '/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()
