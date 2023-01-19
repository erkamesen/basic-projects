import requests
import datetime as dt
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWSAPIKEY = os.getenv('NEWSAPIKEY')
ALPHAAPIKEY = os.getenv('ALPHAAPIKEY')

url1 = "https://www.alphavantage.co/query"
## STEP 1: Use https://www.alphavantage.co

def percent_calculator():
    params={
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "apikey":ALPHAAPIKEY
    }
    response = requests.get(url=url1, params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    datalist = [value for (key,value) in data.items()] #key yazsaydık tarihleri alıcaktık keylere karşılık gelenleri aldık.

    yesterday_data = datalist[0]
    yesterday_closing_price = yesterday_data["4. close"]

    day_before_yesterday_data= datalist[1]  # DÜNÜN DATASI
    day_before_yesterday_closing_price= day_before_yesterday_data["4. close"] # 2 GÜN ÖNCENİN DATASI

    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) #FARK BULMA

    diff_percent = (difference / float(yesterday_closing_price))*100   # YÜZDE BULMA

    return diff_percent

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


now = dt.datetime.now()
tarih = now.date()

params ={
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWSAPIKEY,
}

response = requests.get("https://newsapi.org/v2/everything", params=params)
response.raise_for_status()
dataall = response.json()["articles"]

data = dataall[:3]

news_title = f"TSLA: {round(percent_calculator(),1)}%"
news_description = data[0]["title"].encode("utf-8")
title = news_title.encode("utf-8")



my_email = os.getenv('MY_EMAIL')
password = os.getenv('SMTPKEY')
to_email = os.getenv('TO_EMAIL')

if percent_calculator() > 5:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs=to_email,
                         msg=f"Subject:{title}\n\n{news_description}")




