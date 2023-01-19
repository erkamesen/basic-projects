from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#
nick = "123"
sifrem = "123"
tc = "123"
#
form = Tk()
form.config(bg="burlywood")
form.title("İnternet Arıza Bildirimi")
form.geometry("500x300+750+300")

baslik = Label(form, text="İnternet Şikayet Uygulaması",fg="white" ,bg="burlywood",font=("Times 20 bold"))
baslik.place(x=90, y=10)

# Kullanıcı Adı ve Şifre
giriskullanici = Label(form, text="Kullanıcı Adı: ",fg="white", bg="burlywood", font=("Times 14 bold"))
giriskullanici.place(x=40, y=80)
girissifre = Label(form, text="Şifre: ",fg="white", bg="burlywood", font=("Times 14 bold"))
girissifre.place(x=40, y=120)

ms = messagebox

x = StringVar()
y = StringVar()
gkentry = Entry(form, bg="salmon", textvariable=x, font=("Times 14 bold"))
gkentry.place(x = 180, y=75)
sentry = Entry(form, bg="salmon", textvariable=y, font=("Times 14 bold"),show="*")
sentry.place(x = 180, y=115)

def kontrol2():
    if tckontrol.get() == tc:
        ms.askyesno(title="İşlem Tamam", message="Başvuru Tamamlandı")
        form.destroy()
    else:
        ms.askyesno(title="T.C. Yanlış !!", message="Lütfen Kimlik Nonunuzu Doğru Giriniz.")

def tl():
    global tckontrol
    toplevel = Toplevel()
    toplevel.geometry("350x500")
    toplevel.config(bg="firebrick")
    arizabildirilabel = Label(toplevel, text="Arıza Bildirim Formu", bg="firebrick", font=("Times 20 bold")).pack()
    ls = ["Ad-Soyad: ", "Tc Kimlik No: ", "Modem Tipi: ", "Arıza Tipi: ", "Adres: ", "Mail: "]
    toplam = 70
    for i in range(len(ls)):
        nl = Label(toplevel, text=ls[i], font=("Times 14 bold"), bg="firebrick")
        nl.place(x=20, y=toplam)
        toplam += 60
    ilkentry = Entry(toplevel, bg="pink", font = ("Times 12 bold"))
    ilkentry.place(x=150, y=65)
    tckontrol = StringVar()
    tcentry =  Entry(toplevel, bg="pink", font = ("Times 12 bold"), textvariable=tckontrol)
    tcentry.place(x=150, y=125)
    listee = ["MTPx", "TXPn", "LmnKS", "W8TE", "BOX1"]
    lsbox = ttk.Combobox(toplevel, values=listee, font=("Times 12 bold"))
    lsbox.place(x=150, y=185)
    listee2 = ["Bozuldu", "Kırıldı", "Net yok", "Bu ne la", "Bilmiyom"]
    lsbox = ttk.Combobox(toplevel, values=listee2, font=("Times 12 bold"))
    lsbox.place(x=150, y=245)
    adres = Entry(toplevel, bg="pink", font = ("Times 12 bold"))
    adres.place(x=150, y=305)
    mail = Entry(toplevel, bg="pink", font=("Times 12 bold"))
    mail.place(x=150, y=365)
    buton = Button(toplevel,text="Başvuru Tamamla", activebackground="purple", font = ("Times 12 bold"), command = kontrol2)
    buton.place(x=120, y =425 )

def kontrol():
    global toplevel
    if len(x.get()+y.get())==0:
        ms.askokcancel(title="Hatalı Giriş ! ", message="Kullanıcı Adı veya Parola Boş Bırakılamaz")

    elif x.get() == nick and y.get() == sifrem:
        tl()
    else:
        ms.askokcancel(title="Hatalı Giriş ! ", message= "Kullanıcı Adı veya Parola Hatalı")


kontrol_buton = Button(form, command=kontrol, text="Giriş",font=("Times 16 bold"))
kontrol_buton.config(activebackground="violet")
kontrol_buton.place(x=140, y=180)
iptal_buton = Button(form, command=form.destroy, text="İptal",font=("Times 16 bold"),
                     activebackground="pink").place(x=260, y=180)


# TOPLEVEL PART










form.mainloop()