import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://www.imdb.com/chart/top/"

db = sqlite3.connect("top250imdb.db")
yetki = db.cursor()
db.execute("CREATE TABLE IF NOT EXISTS  FILMS(Sira,Film,Tarih)")

response = requests.get(url=URL)
response.raise_for_status()

veri = BeautifulSoup(response.content, "html.parser")

topveri = veri.find_all("td", {"class":"titleColumn"})

for sira,data in enumerate(topveri, start=1):
    tarih = data.find("span").text.strip("()")
    yetki.execute(f'INSERT INTO FILMS values("{sira}","{data.a.text}","{tarih}")')