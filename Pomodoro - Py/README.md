# Pomodoro

Snap from app:

![Pomodoro 2](https://user-images.githubusercontent.com/120065120/213421820-4218b708-3d4a-4ab3-b761-a200e45971ba.png)

Uygulama bir "Timer" uygulamasıdır. Toplamda 3 adet farklı modu mevcut.

- Work (25 min)
- Break (5 min)
- Long Break (20 min)

Loop şeklinde çalışıyor bir loop içinde toplamda 4 kere "work" (worktotal = 100 min), 4 kere "break" (breaktotal = 5 min), ve en son olarak 1 kere de "Long Break" (longbreaktotal = 20 min) dönüyor.

while True:
	1- Work 
	2- Break
	3- Work
	4- Break
	5-  Work
	6-  Break
	7-  Work
	8-  Break
	9-  Long Break

Pomodoro tekniği hakında daha fazla bilgi için [tıklayınız.](https://tr.wikipedia.org/wiki/Pomodoro_Tekni%C4%9Fi)


Programlama Aşaması :
```py
from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

timer_ = None

  
  

# ---------------------------- TIMER RESET ------------------------------- #

def res():
window.after_cancel(timer_)
canvas.itemconfig(timer_text, text="♫")
global reps
checklabel.config(text="")
reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
	global reps
	reps +=1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	if reps %8 == 0:
		count_down(long_break_sec)
		my_label.config(text="Break", fg=RED)
	elif reps %2==0:
		count_down(short_break_sec)
		my_label.config(text="Break", fg=PINK)
	else:
		count_down(work_sec)
		my_label.config(text="WORK", fg=GREEN)

  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

  

def count_down(count):
	count_min = math.floor(count/60)
	count_sec = count%60
	if 10>count_sec:
		count_sec = f"0{count_sec}"
	if 10>count_min:
		count_min = f"0{count_min}"
		canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global timer_
		timer_ = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		mark = ""
		work_sessions = math.floor(reps/2)
		for i in range(work_sessions):
			mark += "✔"
			checklabel.config(text=mark)

  
  

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")

window.config(padx=100, pady=50, bg="peach puff")

  
  
  

# ADD PHOTO-TEXT WITH CANVAS - PhotoImage CLASS

canvas = Canvas(width=200, height=224, bg="peach puff", highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

  
  

# ADD PHOTO-TEXT WITH CANVAS - PhotoImage CLASS

  

# LABEL

my_label = Label(window,text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg="peach puff")

my_label.grid(column=1, row=0)

  

checklabel = Label(window,text= "", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg="peach puff")

checklabel.grid(column=1, row=3)

  

start_button = Button(text="Start", command = start_timer, bg=GREEN, activebackground=PINK, highlightthickness=0)

start_button.grid(column=0, row=2)

  

rese = Button(text="Reset", command=res, bg=GREEN, activebackground=PINK, highlightthickness=0)

rese.grid(column=2, row=2)

window.mainloop()
```

Kullanılan Kütüphaneler -- tkinter (Tk,Label,Button,Canvas,PhotoImage), Math

Kullanılan Renk Kodları ve Anafont:

PINK = "#e2979c"  
RED = "#e7305b"  
GREEN = "#9bdeac"  
YELLOW = "#f7f5dd"  
FONT_NAME = "Courier"


---------------------------- UI SETUP -------------------------------

Öncelikle Tk classından 1 adet window oluşturup attribute larını belirtiyoruz.(bg, fg, title,
padx, pady)

Tüm widgetlar grid() fonksiyonuyla yerleştirilmiştir.(column = x row = y) 

----------ADD PHOTO-TEXT WITH CANVAS - PhotoImage CLASS----------


Ekrana fotoğraf eklemek için Canvas ve PhotoImage classını kullanıyoruz. 
PhotoImage içindeki "file="" parametresiyle bilgisayar üzerinden her hangi bir fotoğrafın yada resmin 'path' ini belirtiyoruz. (bkz. ""/home/User/Pictures/Tomato.png") file parametresiyle programımıza eklediğimiz fotoğrafımızı ekranımızın üzerine yerleştirmek için 'Canvas' klassını kullanıyoruz.

Programımızda canvasın 2 adet methodundan yararlandık. Domatesi ortaya yerleştirmek için create_image ile x ve y koordinatlarını ayarladık.
create_text ile domatesin üzerindeki yazıyı yazdık.Labelların aksine canvas methodlarında değişiklik yaparken canvas.config yerine canvas.itemconfig adlı bir fonksiyon kullandık.

--------------------------- LABEL ---------------------------

Ekranın top seviyesinde ki o anki modu belirtmek için bir label ve en altta da çalışma modu her bittiğinde bir artan "check mark (✓)" var.
Check marklar reset fonksiyonuyla temizlenmektedir.

--------------------------- BUTTON --------------------------

2 Adet butonumuz mevcut:

-Start command = start_timer ---- : Loopu başlatır 
-Reset command = res ---- : Loopu sıfırlar ve en başa sarar .(Global reps değişkeni en başta 0 değerinde fakat. start_timer fonksiyonu içinde globale çekip her loopda 1 artıyor.)

-------FUNCTIONS-------

*def count_down(count) :*
	Öncelikle zamanı "00:00" şeklinde dijital bir şekilde yazabilmek için. saniye olarak aldığımız count değerini 60 ile bölüyoruz kalanı yuvarlarken daha yakın olsa bile üste değil de tabana çekmek için math kütüphanesinden floor fonksiyonunu kullanıyoruz. Tek haneli olmasın diye if koşuluyla 0 dan 9 a kadar olan kısımda yanına bir 0 ekliyoruz.(Aynı şey saniye kısmı içinde geçerli.)
	Saniye kısmında elimizde olan count verisinin (saniye) 60 moduna bakıyoruz ve kalan bizim saniyemiz oluyor onu da alıyoruz ve zamanı canvas.itemconfig ile değişiyoruz.
	---
	---
	window.after(ms=1000(1 saniye) count_down, count - 1 )
	penceremizi her ms=x saniyede günceliyoruz parametre olarak ilk gecikmeyi yazdım(1).
	2. olarak her 1 saniyede gerçekleştireceği fonksiyonu yazıyoruz. count_down fonksiyonunu vermemizin nedeni de tam olarak bu.. ve asıl olarak fonksiyon parametresinden sonra 1 adet yazdığımız fonksiyonun parametresini yazıyoruz.
	Son olarak count 0 büyükken bu loop dönüyor (recursive fonksiyon), eğer 0 a düşerse else kısmından start_timer() fonksiyonunu tekrar tetikliyoruz ve sonsuz bir döngü yaratıyoruz.

*def start_timer():*
	Programın başında belirttiğimiz reps = 0 değişkenini güncellemek ve bölünebilirliğe göre kullanmak için adım adım modları kullancağımız şekilde global olarak belirtiyoruz ve belirttikten sonra hemen her döngüde +1 olarak artıcak şekilde belirtiyoruz.
	Her modun çalışma süresi farklı olduğu için programın en başında olan süreleri alıp(min cinsinden) 60 ile çarpıp her birini saniyeye çeviriyoruz ve bir değişkene atıyoruz.
	ve koşullarla bir döngü yaratıyoruz. her koşula count_down(xmodusaniyesi) olarak count_down fonksiyonumuzu yerleştiriyoruz. buraya yerleştirdiğimiz komut kendi içinde window.after ile beraber -1 -1 azalıyor ve 0 a ulaştığında modumuz değişiyor. Eğer reps 8 olduysa "long break" modu çalışıyor ve sistem count_down else den gelen start_timer ile tekrardan tetikleniyor. Bu arada window_afterı res fonksiyonunda kullanmak için timerxd adlı bir değişkene atadık.

*def res():*
    window.after_cancel(timerxd)  
	restart butonuna tıkladığımızda tetiklenen bu fonksiyon zamanlayıcı durduruyor.Fakat ekranda süre kalıyor bunu değiştirmek için label.config ile nota işareti yerleştirdim.
	check mark label ı nın textini config ile "" boş string yaptım bu sayede tikler kayboldu.
	global reps belirledim yine ve değerini 0 olarak belirttim. bu sayede start butonuna tekrar tıklandığı zaman kaldığı moddan devam etmektense ilk moda geri dönecek.


