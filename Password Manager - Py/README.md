#proje #python #bootcamp 


Bazen siteler akılda kalıcı şifreleri kabul etmeyebiliyorlar. Bu generator ve manager sayesinde zor ve güvenli şifreleri unutmadan kaydedilebilir ve kullanılabilir.

*Programlama kısmı :*

⭕ Step 1 - Working with Images and Setting up the Canvas:

Öncelikle Canvas ile GUI mize bir adet fotoğraf ekliyoruz.
fotoğrafımız için Canvas keywordlerinden height width 200 200 belirledik.
PhotoImage in file keywordu ile fotoğrafımızı programımıza çekiyoruz.
canvas.create_image ile önce yer belirtiyoruz sonra image= keywordu ile aldığımız fotonun değişkenini atayarak programa aldığımız resimi GUI mize ekliyoruz.

window için config den padx ve pady yi 20 belirledik.

NOT : window.config içindeki highlightthickness keywordu resimden arta kalan parçaları temizlemek için kullanılıyor.
![[pm1.png]]

⭕ Step 2- Use grid() and columnspan to Complete the User Interface:

Renk Paketleri : https://colorhunt.co/

!!! columnspan keywordu grid içnie geliyor ve genişlik girildiği zaman yada her hangi bir widget genişlediği zaman her 2 taraftan(?) genişlediği için ekrana düzgün yayılamıyor ve diğer widgetlarında yerini bozuyor biz uzamasını istediğimiz yöne göre columnspan verirsek o tarafa doğru uzuyor.
(span = açıklık,karış,mesafe,süre)

![[pm2.png]]

Genel olarak tüm widgetları grid() yardımı ile window üstüne ekledim ve column/ row ayarı yaptım. Ek olarak ek te bulunan URL de ki hazır paketlerden GUI me uygun renk seçimini yaptım. Butonlara activebackground ve canvasa highlightthickness uyguladım.

⭕ Step 3- Saving Data to File:

3 Adet Entry classımızdan nesnemiz var ve bunlardan aldığımız bilgileri bir "txt" dosyasına yazmak istiyoruz. Öncelikle entrylerimizden ilki olan website entrysine .focus() adında bir metot uygulayarak pencere açıldığında direkt clicklenmiş gibi imlecin orda olmasını sağlıyoruz. 
Ardından email/username entrysine insert ile beraber (0, "xyz@ mail.com") yazarak önceden kullandığımız mail yada usernameyi oraya kaydediyoruz ki her seferinde tekrar yazmaya gerek kalmasın.Dileğe göre çok sık kullanılan şifre de yazılabilir.


![[pm3.png]]


Add butonunu komutunu belirlemek için addinfos diye bir fonksiyon belirliyoruz.

*def addinfos():*
	Öncelikle entrylerin boş olup olmadığını kontrol etmek için bir koşula sokuyoruz ve uzunlukları eğer 0 ise mssageboxın uyarı panelinden bir mesajı ekrana getiriyoruz.
	else:
	entryden aldığımız bilgileri open komutuyla bulunduğumuz dizin içine bir registerinfo.txt dosyası açarak append ediyoruz(append modunda eğer o adda bir dosya yoksa dosyayı açar tıpkı w modunda olduğu gibi ancak w modundan en önemli farkı eğer bir dosya zaten varsa yeni bilgileri üsüne ekler)
	Ardından entrylerimizin üstünde kalan artık yazıları temizleyi yeni bir girişe hazır ediyoruz.
	!!!! Ek olarak başta bilgileriniz bunlar diyen bir messagebox daha ekledim tam else koşulundan sonra metot ismi askokcancel, True ve False değeri alıyor bu sayede bir if koşulu daha yazdım eğer ok a basılırsa işlem tamam cancel basılırsa txt dosyasına kaydetmiyor.

⭕ Step 4- Generate a Password & Copy it to the Clipboard:

![[pm4.png]]

Öncelikle eskiden yaptığımız password_generator dosyasını programımıza kopyalıyoruz.
Birazcık düzenleme yapıp list comprehence kullanarak listelerimizi oluşturuyoruz. for loopu kalabalığından kurtuluyoruz.
!!!!!!!!! PASSWORD GENERATORU ilk başta fonksiyon oluşturmadan dışarıdan import ettim lakin hep aynı harfler arasında döndü şifrelerim.Bir şekilde oldu diye sevindim ama aynı harflerin loopa sardığını görünce bir tık üzüldüm yalan yok :)
Ardından her tıklayışımızda fonksiyon çalıştığı için yeni bir password değeri üretildi ve her seferinde çok alakasız harflerle bir veri almayı başardım.Demem o ki fonksiyon kullanmak gerçekten önemli.

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


