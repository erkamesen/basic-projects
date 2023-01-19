import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv('MY_EMAIL')
SMTPkey = os.getenv('SMTPKEY')
to_email = os.getenv('TO_EMAIL')
MY_LAT = 41.195759  # Your latitude
MY_LONG = 32.621712  # Your longitude
def is_True():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG +5:
        return True

def is_night() :
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if not sunrise <= time_now.hour <= sunset:
        return True

while True:
    time.sleep(60)
    if is_True() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg="Subject:Look UP\n\nThe ISS is above you in the sky ")

# BONUS: run the code every 60 seconds.



