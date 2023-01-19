import pandas as pd
import datetime as dt
import random , smtplib
from dotenv import load_dotenv
import os 

load_dotenv()

my_email = os.getenv('YOUREMAIL')
password = os.getenv('SMTPKEY')    # GOOGLE 16 HANELİ UYGULAMA ŞİFRESİ
to_email = os.getenv('TOEMAIL')

# Gün kontrolü
now = dt.datetime.now()
with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as fs:
    icerik = fs.read()
data = pd.read_csv("birthdays.csv")
sozluk = data.to_dict(orient="records")

for i in range(len(sozluk)):
    if sozluk[i]["day"] == now.day and sozluk[i]["month"] == now.month:
        yeniicerik = icerik.replace("[NAME]", sozluk[i]["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=my_email, password=password)
            connect.sendmail(from_addr=my_email,
                             to_addrs=sozluk[i]["email"],
                             msg=f"Subject:HAPPY BIRTHDAY\n\n{yeniicerik}" )
