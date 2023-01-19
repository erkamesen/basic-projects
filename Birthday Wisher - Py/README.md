# Birthday Wisher


*Kullandığım kütüphaneler:*
>import pandas as pd  
import datetime as dt  
import random , smtplib

 
 
#### Mektupları Tanıtmak
3 adet doğum günü mektubumuz var farklı .txt dosyaları içinde bunları with ve read ile çekiyoruz

```py
with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as fs:  
    icerik = fs.read()
```

*random.randint(1,3)* yardımıyla rastgele seçiyoruz.


>Dear [NAME],  
>Happy birthday!  
>All the best for the year!  
>Angela
  

---
#### Sabitleri Belirlemek

Mailleri ve uygulama passwordunı değişkenlere atıyoruz.
[[smtplib - pythonanywhere#smtplib|smtplib]]

```py
my_email = YOURMAIL 
password = SMTPKEY   # GOOGLE 16 HANELİ UYGULAMA ŞİFRESİ  
```


#### CSV Dosyasını Okumak

```py
name,email,year,month,day  
Muzaffer,erkamesen789@yahoo.com,1994,10,29  
Munevver,erkamesen789@yahoo.com,1960,10,25
```
Şeklinde bir *.csv* dosyamız var burdan bilgileri çekmek için *pandas* kütüphanesini kullandım.

```py
data = pd.read_csv("birthdays.csv")  
sozluk = data.to_dict(orient="records")
```

pandas ile okuduğum dosyayı python içinde kullanabilmek için sözlüğe dönüştürdüm indexleri yok etmek için *orient="records"* kullandım

```py
[{'name': 'Muzaffer', 'email': 'erkamesen789@yahoo.com', 'year': 1994, 'month': 10, 'day': 29}, {'name': 'Munevver', 'email': 'erkamesen789@yahoo.com', 'year': 1960, 'month': 10, 'day': 25}]

```

Liste içinde 2 adet sözlük var her row bir sözlük olarak ayrılıyor ve sözlüğün başlıkları ise rowun kendi başlığı oluyor.

Artık elimizde efektif şekilde kullanabileceğimiz bir sözlük olduğuna göre artık mailimizi yolayabiliriz.

#### datetime ve smtp

```py
now = dt.datetime.now()
```

şuanın tarihini alıyorum *now.day*  ve *now.month* metodlarıyla bulunduğumuz günü ve ayı alıp csv dosyasından aldığımız bilgilerin gün ve aylarıyla karşılaştırabileceğiz.

Sözlüğümüzün bulunduğu listemizi len() sayısına göre for dögüsüne sokuyoruz.

```py
for i in range(len(sozluk)):  
    if sozluk[i]["day"] == now.day and sozluk[i]["month"] == now.month:  
        yeniicerik = icerik.replace("[NAME]", sozluk[i]["name"]).replace("Angela", "Erkam")  
        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:  
            connect.starttls()  
            connect.login(user=my_email, password=password)  
            connect.sendmail(from_addr=my_email,  
                             to_addrs=sozluk[i]["email"],  
                             msg=f"Subject:HAPPY BIRTHDAY\n\n{yeniicerik}" )
```

*i* burda 2 tane değer alıyor 0 ve 1.
i 0 yada 1 ken günümüze ve monthumuza bakıyoruz ve bu günle karşılaştırıyoruz eğer eşleşiyorsa koşul sağlanıyodur ve alt satıra geçiyoruz.
with metoduyla SMTP serverimizi açıyoruz portumuz yerleştirip değişkene atıyoruz.
ardından *starttls* ile güvenliğimizi alıyoruz login işlemi yapıp sendmail ile mesajımızı yolluyoruz.

![[wisherotomasyon.png]]

Eğer istersek [[smtplib - pythonanywhere#pythonanywhere|pythonanywhere]] ile web üzerinden belirli bir düzende maili de yollayabiliriz. 
