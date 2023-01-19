# Password Manager


Bazen siteler akılda kalıcı şifreleri kabul etmeyebiliyorlar. Bu generator ve manager sayesinde zor ve güvenli şifreleri unutmadan kaydedilebilir ve kullanılabilir.

*Programlama kısmı :*


⭕ Resimler ve Canvas

Öncelikle Canvas ile GUI mize bir adet fotoğraf ekliyoruz.
fotoğrafımız için Canvas keywordlerinden height width 200 200 belirledik.
PhotoImage in file keywordu ile fotoğrafımızı programımıza çekiyoruz.
canvas.create_image ile önce yer belirtiyoruz sonra image= keywordu ile aldığımız fotonun değişkenini atayarak programa aldığımız resimi GUI mize ekliyoruz.

```py
window = Tk()
window.config(bg="#FAD6A5", padx=50, pady=50, highlightthickness=0)
window.title("Password Manager")

canvas = Canvas(height=200, width=200,bg="#FAD6A5", highlightthickness=0)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0)

window.mainloop()
```

window için config den padx ve pady yi 20 belirledik.

NOT : window.config içindeki highlightthickness keywordu resimden arta kalan parçaları temizlemek için kullanılıyor.



⭕ Step 2- Use grid() and columnspan to Complete the User Interface:

Renk Paketleri : https://colorhunt.co/

!!! columnspan keywordu grid içnie geliyor ve genişlik girildiği zaman yada her hangi bir widget genişlediği zaman her 2 taraftan(?) genişlediği için ekrana düzgün yayılamıyor ve diğer widgetlarında yerini bozuyor biz uzamasını istediğimiz yöne göre columnspan verirsek o tarafa doğru uzuyor.
(span = açıklık,karış,mesafe,süre)

![pm2](https://user-images.githubusercontent.com/120065120/213446910-0ffd4c12-882a-41ff-a229-3ee7cba457a6.png)

Genel olarak tüm widgetları grid() yardımı ile window üstüne ekledim ve column/ row ayarı yaptım. Ek olarak ek te bulunan URL de ki hazır paketlerden GUI me uygun renk seçimini yaptım. Butonlara activebackground ve canvasa highlightthickness uyguladım.

⭕ Step 3- Saving Data to File:

3 Adet Entry classımızdan nesnemiz var ve bunlardan aldığımız bilgileri bir "txt" dosyasına yazmak istiyoruz. Öncelikle entrylerimizden ilki olan website entrysine .focus() adında bir metot uygulayarak pencere açıldığında direkt clicklenmiş gibi imlecin orda olmasını sağlıyoruz. 
Ardından email/username entrysine insert ile beraber (0, "xyz@ mail.com") yazarak önceden kullandığımız mail yada usernameyi oraya kaydediyoruz ki her seferinde tekrar yazmaya gerek kalmasın.Dileğe göre çok sık kullanılan şifre de yazılabilir.

```py
def addinfos():

    newdatadict = {website_entry.get():
                   {"email":username_entry.get(),
                    "Password":password_entry.get()}
               }
    if len(website_entry.get()) < 1 or len(username_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.askokcancel(title="Uyarı", message="Lütfen Belirtilen Alanları Boş Bırakma")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"There are the details entered: \nEmail {username_entry.get()} \n"
                                               f"Password : {password_entry.get()} \nIs it")
        if is_ok:
            try:
                with open("registerinfos.json", "r") as data_file:

                    # READING OLD DATA
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("registerinfos.json", "w") as data_file:
                    json.dump(newdatadict, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(newdatadict)
                with open("registerinfos.json", "w") as data_file:
                    #Saving uptadet data
                    json.dump(data, data_file, indent=4)
            finally:
                username_entry.delete(0, END)
                password_entry.delete(0, END)
```


Add butonunu komutunu belirlemek için addinfos diye bir fonksiyon belirliyoruz.

*def addinfos():*
	Öncelikle entrylerin boş olup olmadığını kontrol etmek için bir koşula sokuyoruz ve uzunlukları eğer 0 ise mssageboxın uyarı panelinden bir mesajı ekrana getiriyoruz.
	else:
	entryden aldığımız bilgileri open komutuyla bulunduğumuz dizin içine bir registerinfo.txt dosyası açarak append ediyoruz(append modunda eğer o adda bir dosya yoksa dosyayı açar tıpkı w modunda olduğu gibi ancak w modundan en önemli farkı eğer bir dosya zaten varsa yeni bilgileri üsüne ekler)
	Ardından entrylerimizin üstünde kalan artık yazıları temizleyi yeni bir girişe hazır ediyoruz.
	!!!! Ek olarak başta bilgileriniz bunlar diyen bir messagebox daha ekledim tam else koşulundan sonra metot ismi askokcancel, True ve False değeri alıyor bu sayede bir if koşulu daha yazdım eğer ok a basılırsa işlem tamam cancel basılırsa txt dosyasına kaydetmiyor.

⭕ Step 4- Generate a Password & Copy it to the Clipboard:

```py
def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letterslist = [choice(letters) for _ in range(randint(8, 10))]
    numberslist = [choice(numbers) for _ in range(randint(2, 4))]
    symbolslist = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letterslist + numberslist + symbolslist

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

```

Öncelikle eskiden yaptığımız password_generator dosyasını programımıza kopyalıyoruz.
Birazcık düzenleme yapıp list comprehence kullanarak listelerimizi oluşturuyoruz. for loopu kalabalığından kurtuluyoruz.


*def generatepass():
	xx letters listesinden 8 - 10 arası harf alıp letterslist adlı bir listeye ekliyoruz
	xx number listesinden 2 - 4 arası rakam alıp numberslist listesine ekliyoruz
	xx symbols listesinden 2 - 4 arası işaret alıp symbolslist listesine ekliyoruz
	Ardından bu 3 listeyi toplayarak tek 1 tane liste elde ediyoruz ve onu password_list adında bir değişkene atıyoruz.
	Ard arda toplandığı için sıralı bir şekilde devam eden bu listeyi shuffle metoduyla güzelce bir karıştırıyoruz.
	.join() metoduyla listeyi bir stringe çeviriyoruz ve password adlı değişkene atıyoruz.
	Şifreler üst üste binmesin diye her basışta entryi 0, END şeklinde baştan sona deleteliyoruz.
	Yeni şifreyi oluşturuyoruz.
	pyperclip.copy(password) metoduyla her generate de şifreyi Ctrl + C ye alıyoruz.


