#python #proje #bootcamp 


![[flashy1.png]]


Program için veri girişini *.txt* dosyasından yaptım.
French-English yerine Turkish-English şeklinde çevirdim. Günlük hayatta en sık kullanılan 5000 ingilizce kelimeyi kullandım.







#### Create the User Interface (UI) with Tkinter

```py
window = Tk()  
window.title("Flashy")  
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  
  
canvas = Canvas(width=800, height=526)  
card_front_img = PhotoImage(file="./images/card_front.png")  
canvas.create_image(400, 263, image=card_front_img)  
canvas.create_text(400,150, text="Title", font=TITLEFONT)  
canvas.create_text(400, 263, text="word", font=WORDFONT)  
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)  
canvas.grid(column=0, row=0, columnspan=2)  
  
cross_image = PhotoImage(file="./images/wrong.png")  
unknown_button = Button(image=cross_image)  
unknown_button.grid(row=1, column=0)  
  
check_image=PhotoImage(file="./images/right.png")  
known_button = Button(image=check_image)  
known_button.grid(row=1, column=1)  
  
window.mainloop()
```

İlk olarak  Tk classından penceremizi oluşturup gerekli kalan işlemleri hallettik.(Tittle, padx, pady, bg)

##### CANVAS
Ardından Canvas classından bir adet nesne ürettik ve bu nesneyi 1 adet resim ( Beyaz olan) ve 2 adet yazı üretmek için kullandık. Fotoğrafın boyutu *width=800* *height=526*
olduğu için direkt class oluştururken attribute olarak bunu belirleyip tuval boyutumuzu ayarladık. Sonra PhotoImage ile file path vererek fotoğrafımızı programımıza çektik.
Ve artık fotoğrafımız tuvale eklenmeye hazır hale geldi. *create_image* fonksiyonu içine ilk oalrak koordinat vermemiz gerekiyor. *x=width/2* *y=height/2* olduğu için *400 263*  olarak koordinatlarımı girdim ve ardından *image=resim* ile fotoğrafı ekledim.

> [!WARNING] AŞIRI DİKKAT
> *file=* olsun* image=* olsun bu attribute ları vermeyi unutma.


Ardından aynı objeyle yazı üretebildiğimizi öğrendim ve *create_text* metodu ile 2 adet yazı ürettim. üretirken direkt *x* ve *y* koordinatlarını yazıyoruz ve oraya gidiyolar. 

Son olarak grid le yerleştirdim fakat en sonunda sola doğru bi kayma olduğu için *columnspan = 2* olarak belirttim.

##### BUTTON

yine PhotoImage yardımı ile 2 adet buton resmimi çektim. Butonların *image=* attribute u olduğunu öğrendim. tek yapmamız gereken resmi çektikten sonra buton classından 2 tane obje üretip bu objelerin image= attributelarına resim yazmak oldu.

Grid ile birini *(column=0 row=1)* diğerini *(column=1 row=1)* yerlerine yolladım ve ilk kısmı bitirdim.

---


#### Create New Flash Cards


```py
card_title = canvas.create_text(400, 150, text="", font=TITLEFONT)  
card_word =canvas.create_text(400, 263, text="", font=WORDFONT)
```

öncelikle canvas objemizle oluşturduğumuz text itemlerini 2 adet değişkene atadık.
ve textlerini değiştik çünkü fonksiyonda değiştiridğimiz textleri en sonunda fonksiyonu mainloop dan bi önceki adım kullanarak kullanıcıya direkt olarak kelimenin ve dilin gelmesini sağladık.

```py
def next_card():  
    kelime=random.choice(trwords)  
    canvas.itemconfig(card_title, text="Turkish")  
    canvas.itemconfig(card_word, text=kelime)
```

fonksiyon ilk adımda türkçe kelimeler listesinden rastgele bir kelime seçiyor ve asıl olayın olduğu fonksiyon başlıyor.

##### canvas.itemconfig(item, itemattribute)

öncelikle fonksiyonu yazdıktan sonra ilk başta değiştirmeyi istediğimiz itemin ismini yazıyoruz ve ardından değiştirmeyi istediğimiz özelliğini yazıyoruz.
Şuanlık fonksiyonu known ve unknown butonlarına atadık. Her basışta farklı bir kelime getiriyor.


#### Flip Cards

```py
def next_card():  
    kelime=random.choice(trwords)  
    global correctword, flip_timer  
    window.after_cancel(flip_timer)  
    correctword = wordicttr[kelime]  
    global wrongword  
    wrongword = random.choice(engwords)  
    canvas.itemconfig(card_background, image=card_front_img)  
    canvas.itemconfig(card_title, text="Turkish", fill="black")  
    canvas.itemconfig(card_word, text=kelime.title(), fill="black")  
    flip_timer = window.after(3000, func=flip_card)  
  
def flip_card():  
    canvas.itemconfig(card_background, image=card_back_img)  
    canvas.itemconfig(card_title, text="English", fill="white")  
    canvas.itemconfig(card_word, text=correctword)

window = Tk()  
window.title("Flashy")  
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  
  
flip_timer = window.after(3000, func=flip_card)
```


Öncelikle her 3 saniyede bir değişmesi için window.after ı 3000 ms yapıyoruz ve bunu bir değişkene atıyoruz. Arından *func=* için flip_card adında bir fonkisyon oluşturuyoruz ve Türkçe kelime den 3 saniye sonra ingilizce kelimeyi ekranda gösteriyor. itemconfig ile canvas dan atadığımız title word ve image yi değiştiriyoruz. ardından tekrar Türkçe karta geri döneceği için orayı da eski haline itemconfigle geri getiriyoruz. next_card içinde *global  flip_timer* .Butonlara her basıldığında kelime değişiyor fakat zamanlayıcı değişmiyor.onun için next_card fonksiyonuna *window.after_cancel(flip_timer)* ekledik. Fonksiyon her çalıştığında zamanlayıcı iptal oluyor. fakat fonksiyonun en sonuna tekrardan flip_timer eklendiğinden aynı zamanda fonksiyon her çalıştığında(butona her basıldığında süre yeniden başlıyor.)

#### Save Progress

```py
def is_known():  
    with open("to_learn.csv") as data_learn:  
        deneme = csv.DictReader(data_learn)  
        if kelime not in deneme:  
            with open("to_learn.csv", "a", encoding="UTF-8") as f:  
                to_learn.update(nd)  
                for key,value in to_learn.items():  
                    f.write(f"{key},{value}\n")  
                to_learn.clear()  
  
  
    next_card()
```

beyin bir tık yandı ama son olarak yaptığımı açıklamak gerekirse (try,except ile de dosyayı açabilirdim fakat manuel açtım karışsın istemedim.) öncelikle csv dosyasını okuyoruz. ve içindekini deneme adlı bir değişkene sözlük olarak atıyoruz.
DEĞİŞCEK DEĞİŞCEK

eğer kelime dosya içinde yoksa dosyaya csv olarak word,word olarak kaydediyoruz.
