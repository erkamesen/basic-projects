# Stock News Tracker

Belirttiğimiz miktarda yüzdelik değişim olduğunda otomatik olarak mail atıcak python botu.

*Kütüphaneler:*

```py
import requests  
import datetime as dt  
import smtplib
```


*Sabitler:*

```py
STOCK = "TSLA"  
COMPANY_NAME = "Tesla Inc"  
NEWSAPIKEY = YOURAPIKEY  
ALPHAAPIKEY = YOURAPIKEY
---
my_email = YOUREMAIL 
password = YOURSMTPKEY  
to_email = TOEMAIL
```


*APILER:

```py
"https://www.alphavantage.co/query"
"https://newsapi.org/v2/everything"
```

1. alphaavantage ile stok takibi yapılabilir.
2. newsapi ile haberler alınabilir.


#### Stok Takibi

```py
def percent_calculator():  
    params={  
        "function":"TIME_SERIES_DAILY",  
        "symbol":STOCK,  
        "apikey":ALPHAAPIKEY  
    }  
    response = requests.get(url="https://www.alphavantage.co/query", params=params)  
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
```

öncelikle [site](https://www.alphavantage.co/documentation/) nin documentation kısmından *Tesla* hisse senedi için doğru parametreleri arıyoruz.

*Symbol = STOCK= "TSLA"* kısmı istediğimiz verinin sembolü.
*function="TIME_SERIES_DAILY"* ise site tarafından zaten veriliyor.


1. sitenin endpointine request atıyoruz ve response adlı değişkene cevabımızı atıyoruz.
2. *raise_for_status()* ile servis durumunu kontrol ediyoruz.
3. *data = response.json()("Time Series (Daily)")* ile günlüğümüzün kullanılıcak kısmına giriyoruz.
4. list comprehesion ile keyleri atıp sadece *valueları* listemize alıyoruz.(Burada keyler tarih)
5. Yüzdelik değişimi (%) belirlemek için *dünün ve ondan önceki günün close*(kapanış) saatlerini ele alıyoruz.
6. Farkı mutlak bir şekilde bir değişkene atıyoruz. Değerlerimiz str olarak bize geldiği için floata çeviriyoruz işlem yaparken.
7. yüzdelik değişimi hesaplamak için çıkan farkı dünün kapanış değerine bölüyoruz ve çıkan sonucu 100 ile çarpıyoruz.
8. *diff_percent = (difference / float(yesterday_closing_price))x100*
9. diff_percenti return ediyoruz.


#### Haberleri Alma

Değişimi kendimize mail olarak alıcaz tamam ama bir de bu değişime sebep olan şeyi de görmek ister insan tabikide.
Bu yüzden gelen mailde takibe aldığımız verinin gündemde olan son haberlerinden bir kesit bize mail geliyor.
[site](https://newsapi.org/)

```py
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
```


1. Tarihi günlük haber almak için kullanabiliriz ama gece 12 den sonra sıfırlandığı için haber bulamazsa veri çekemeyip hata veriyor.(Hata yakalama ile çözülebilir.)
2. parametreler şirket ismi ve APIkey
3. Sitenin endpointine request atıyoruz ve gelen cevabı response ediyoruz ardından json formatında bir değişkene atıyoruz.
4. Liste çok fazla uzun olduğu için slicing ile ilk 3 haberi alıyoruz.
5. f-string metodu ile *başlık* ve *içeriklerden* mailimize *subject* ve *body* hazırlıyoruz.
6. Elimizde olan *string veriye* mailimzide hata vermesin diye *.encode("utf-8")*  metodunu uygulayarak hatadan kaçıyoruz.

#### Mail atma

```py
my_email = YOUREMAIL
password = SMTPKEY 
to_email = TOEMAIL
  
if percent_calculator() > 5:  
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect:  
        connect.starttls()  
        connect.login(user=my_email, password=password)  
        connect.sendmail(from_addr=my_email,  
                         to_addrs=to_email,  
                         msg=f"Subject:{title}\n\n{news_description}")
```

Eğer değişim istediğimiz miktara geldiyse koşul gerçekleşiyor ve python bize bir mail atıyor.

1. *with smtplib.SMTP("smtp.gmail.com", port=587) as connect:* ile mail atmak için kendimize bir blok oluşturyoruz.
2. *starttls()* ile güvenliğimizi sağlıyoruz.
3. *login(... ...)*  ile hesabımıza giriş yapıyoruz.
4. *sendmail* ile mesajımızı yolluyoruz.
