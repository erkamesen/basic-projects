import requests
from bs4 import BeautifulSoup


response = requests.get("http://erkamesen.com/")
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser") #response umuzu html.parser ile parselliyoruz

# yazdir = soup.html # TÜM SAYFAYI ÇEKİYORUZ
# print(yazdir)

# yazdir = soup.body #SADECE BODY KISMINI ÇEKİYORUZ
# print(soup)

# yazdir = soup.head.title.text #WEBSİTE İÇİNDEKİ HEAD İÇİNDEKİ TİTLE VER
# print(yazdir)   #SONUNA TEXT KOYMAZSAK TAGLERIDE GOSTERIYOR YAZDIRIRKENDE KOYULABİLİR
#

# yazdir = soup.body.h2.text #BAŞLIĞI YAZDIRDIK
# print(yazdir)

# yazdir = soup.body.p.text
# print(yazdir) #PARAGRAFI ALDIK AMA 1 TANE


# yazdir = soup.find("p").text #ARADIĞIMIZ NİTELİKTEKİ İLK VERİYİ SADECE 1 TANE
# print("-"*80)
# print(yazdir)

# yazdir = soup.find_all("p")
# for paragraf in yazdir:
#     print("-"*80)
#     print(paragraf.text)    # TÜM PARAGRAFLARI ÇEKME

# yazdir = soup.find_all("h3") #BAŞLIKLAR ÇEKLIYOR h1 h2 h3 h4 h5
# for baslik in yazdir:
#     print("-"*40)
#     print(baslik.text)

#### NİTELİĞE GÖRE VERİ ÇEKME

# div_cek = soup.find_all("div")
# for divs in div_cek:
#     print("-"*40)
#     print(divs.text) #TÜM div LER


# div_cek = soup.find("div", {"class":"wp-block-group__inner-container"}).text
# print(div_cek)

div_cek = soup.find("div",{"class":"footer-copyright"}).a
print(div_cek.get("href"))
#result = https://scriptstown.com/ # div içindeki a etiketinden hrefi get ile çektik




