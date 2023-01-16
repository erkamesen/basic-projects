from bs4 import BeautifulSoup
import requests
from infosfordataautomation import URL



class Zillow:
    def __init__(self):
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
            "Accept-Language":"en-US,en;q=0.5"
        }
        response = requests.get(URL, headers=self.header)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")

        self.prices = []
        self.links = []
        self.address = []




    def getPrices(self):
        prices = self.soup.find_all("div", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX")
        for _ in prices:
            price = _.text.strip()
            if "+" in price:
                self.prices.append(price.split("+")[0])
            else:
                self.prices.append(price.split("/")[0])
        return self.prices

    def getLinks(self):
        links = self.soup.find_all("a", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link", href=True)
        for _ in links:
            link = _["href"]
            if link.startswith("http"):
                self.links.append(link)
            else:
                self.links.append(f"https://www.zillow.com{link}")

        return self.links

    def getAddress(self):
        addresses = self.soup.find_all("address", {'data-test':"property-card-addr"})

        for _ in addresses:
            self.address.append(_.text)

        return self.address


