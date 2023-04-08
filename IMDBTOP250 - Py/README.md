# IMDBTOP250

![Seçim_015](https://user-images.githubusercontent.com/120065120/213432503-e4e84da9-3e7e-4c8e-a4a5-0f59bb97c12f.png)

*Libraries:*

```py
import requests  
from bs4 import BeautifulSoup  
import sqlite3
```

*KODLAR*

```py
URL = "https://www.imdb.com/chart/top/"  
  
db = sqlite3.connect("top250imdb.db")  
yetki = db.cursor()  
# yetki.execute("CREATE TABLE IF NOT EXISTS  FILMS(Sira,Film,Tarih)")  
  
response = requests.get(url=URL)  
response.raise_for_status()  
  
veri = BeautifulSoup(response.content, "html.parser")  
  
topveri = veri.find_all("td", {"class":"titleColumn"})  
  
[for sira,data in enumerate(topveri, start=1):  
	tarih = data.find("span").text.strip("()")
    yetki.execute(f'INSERT INTO FILMS values("{sira}","{data.a.text}","{tarih}")')>)
```


Öncelikle URL adlı değişkenimize veri çekeceğimiz endpointimizin linkini atıyoruz.

Databese kısmı için ise *sqlite3.connect("isim.db")* ile db değişkenimiz ile eğer o adda bir database varsa bağlıyoruz yoksa isim.db şeklinde bir database açıyoruz.
*yetki=db.cursor()* ile yetki veriyoruz.


> *yetki.execute("CREATE TABLE IF NOT EXISTS  TABLOISMI(row1, row2)")*

ile bir tablo ve sütunlar oluşturuyoruz.



requests işlemleriyle sitemize bağlanıyoruz. Fakat requests modülü bize siteyi html kaynak kodlarıyla yani bir insan tarafından okunması çok zor bir şekilde getiriyor.Bu sebeple yardmımıza bs4 koşuyor.

*veri = BeutifulSoup(response.content, "html.parser")* ile html mizi inciğine kadar parçalıyoruz ve veri adlı değişkene bunları atıyoruz.

Veri çekmek istediğimiz siteden html kaynak kodları içinden istediğimiz bölümü buluyoruz ardından *.find("etkiket ismi", {class : class ismi})* ile aradığımız niteliği çekebiliyoruz. Lakin biz burda 250 adet veri çekeceğimiz için *.find_all()* kullandık bu sayede bize hepsini verdi.

Elimize geçen bilgileri daha detaylı görmek için data.a ile "*a*" etiketlerinin de içine giriyoruz fakat elimizde olan veri hala etiketli şekilde bu yüzden *data.a.text* ile tam olarak istediğimiz veriyi elde ediyoruz.

Artık elimizde for döngüsüyle aldığımız 250 adet efsanevi film var şimdi bunları yine for döngüsü sayesinde her döngüde teker teker veritabanımıza pushlayabiliriz.

>yetki.execute(f'INSERT INTO FILMS values("{sira}","{data.a.text}","{tarih})')

f-string yardımı ile yine *.execute()* kullanarak FILMS tablomuzun içine bilgileri sütun sütun insertliyoruz.



![Seçim_015](https://user-images.githubusercontent.com/120065120/230721293-2c677fd0-29bf-489f-a3ab-cd1647a8bf0a.png)


*DB Browser for SQLite*


