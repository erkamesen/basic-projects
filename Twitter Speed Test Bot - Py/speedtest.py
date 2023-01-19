from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Speedtest:
    def __init__(self) -> None:
        # BURAYA chromedriver.exe PATHI GELECEK
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        s = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(options=options ,service=s)
        self.URL = "https://www.speedtest.net/"
        self.infos = {}

    def openPage(self):
        """
        Sadece sayfayı açıyor ve tam ekran haline getiriyor.
        :return driver.:
        """
        self.driver.get(self.URL)
        self.driver.maximize_window()


    def clicker(self, xp):
        self.driver.find_element(By.XPATH, xp).click()

    def getSpeedInfos(self):
        download = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                      '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                      '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        requestID = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                      '/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
        generalping = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                      '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text
        ISS = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                      '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[2]/div[2]/a').text

        self.infos.update({
            "download":download,
            "upload":upload,
            "requestID":requestID,
            "Ping":generalping,
            "ISS":ISS
        })

        return self.infos

    def closeSpeedtest(self):
        self.driver.quit()
