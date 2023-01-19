#python #proje #bootcamp 


Kullandığım kütüphaneler
```py
import requests  
from datetime import datetime  
import smtplib  
import time
```

CONSTANT
```py
my_email = YOUREMAIL 
password = SMTPKEY
to_email = TOMAIL
MY_LAT = 41.195759  # Your latitude  
MY_LONG = 32.621712  # Your longitude
```

*latitude = enlem
longitude = boylam*

Karabük iline ait enlem ve boylamı [siteden](https://www.latlong.net/) aldım. 

Şartlar

1. Your position is within +5 or -5 degrees of the ISS position.
2. If the ISS is close my current position.
3. And it's currently dark.
4. Than send me an email to tell me to look up.
5. BONUS Run the code every 60 seonds.


#### ISS Yakınlarda mı ?

```py
def is_True():  
    response = requests.get(url="http://api.open-notify.org/iss-now.json")  
    response.raise_for_status()  
    data = response.json()  
  
    iss_latitude = float(data["iss_position"]["latitude"])  
    iss_longitude = float(data["iss_position"]["longitude"])  
    #Your position is within +5 or -5 degrees of the ISS position.  
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG +5:  
        return True
```

Öncelikle ISS in bulunduğu konumu öğrenmek için API yi aldığımız [siteye](http://api.open-notify.org/iss-now.json) bir request atıp gelecek cevabı response adlı bir değişkene atıyoruz.
*response.raise_for_status()* ile gelecek her hangi bir 404 tarzı hata için yakalama yapıyoruz.
Aldığımız bu bilgiyi json formatında data adlı bir değişkene atıyoruz.

iss_latitude ve iss_logitude adında 2 adet değişkene sözlüğümüzden keyleri kullanarak float değerleri aktarıyoruz.

kendi pozisyonumuz +5 -5 durumu ile ISS position ı karşılaştırıyoruz ve eğer bu 5 lik içindeyse fonksiyonumuz *True* değer döndürüyor.

#### Gece mi ?

```py
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
```

API yi aldığımız [site](https://api.sunrise-sunset.org/json)  bize parametreleri sözlük şeklinde vermemiz gerektiğini söylüyor.

##### Parameters

-   **lat** (float): Latitude in decimal degrees. Required.
-   **lng** (float): Longitude in decimal degrees. Required.
-   **date** (string): Date in YYYY-MM-DD format. Also accepts [other date formats](https://php.net/manual/en/datetime.formats.date.php) and even [relative date formats](https://php.net/manual/en/datetime.formats.relative.php). If not present, date defaults to current date. Optional.
-   **callback** (string): Callback function name for JSONP response. Optional.
-   **formatted** (integer): 0 or 1 (1 is default). Time values in response will be expressed following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) and day_length will be expressed in seconds. Optional.

parametrelerimiz kendi latitude ve longitude miz. Formatted ile datetime dan aldığımız zaman ile aynı şekle getiriyoruz.

siteye request atıp response adlı değişkene cevabı atıyoruz.

ardından cevabı *json()* ile data adlı değişkene atıyoruz.

sunrise ve sunset için data değişkenimizin *"results","sunrise(set)"* olmak üzere 2 kere key değiştirip değerlerimizi int şekilde alıyoruz. (1, 13, 11)

*time_now = datetime.now().hour* ile saatimizin int halini alıyoruz.

*if not sunrise <= time_now.hour <= sunset:* ile beraber saatimizin gündoğumu ile günbatımı arasında olmadığı zamanı yani gece vaktini kontrol ediyoruz ve *True *döndürüyoruz.

```py
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0

Linklerdeki ana url den sonraki lat , lng , formatted bizim PARAMETRELERİMİZ.

https://api.sunrise-sunset.org/json, param=parameters yapabiliriz

```


#### Mail atma

```py
while True:  
    time.sleep(60)  
    if is_True() and is_night():  
        with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:  
            connection.starttls()  
            connection.login(my_email, password=password)  
            connection.sendmail(from_addr=my_email,  
                                to_addrs=to_email,  
                                msg="Subject:Look UP\n\nThe ISS is above you in the sky ")
```

eğer 2 fonksiyonumuzdan *True* değerini alırsak smtplib ile bağlanıp kendimize gökyüzüne bak diye bir mail atıyoruz.


