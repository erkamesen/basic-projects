from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox

form = Tk()
resim = ImageTk.PhotoImage(Image.open('direnc.png'))
form.title("Direnc Degeri Hesaplama")

# buton = Button(form, image=resim)
# buton.pack()
label = Label(form, image=resim)
label.config()
label.pack()




# 4 BANTLI

label_4= Label(form, text= "4-5-6 Bantli Direncler icin Renk Kodu Okuma", bg="black", fg="white", font=('Times 14 bold')).place(x=40 ,y=90)

#KUTU 1
liste = ['Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu1 = Combobox(form, values=liste)
kutu1.place(x=10, y=130, width =70)
#KUTU 2
listem = ['Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu2 = Combobox(form, values=listem)
kutu2.place(x=100, y=130, width =70)
#KUTU 3
liste2 = ['Gumus',  'Altin', 'Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi']
kutu3 = Combobox(form, values=liste2)
kutu3.place(x=190, y=130, width =70)
#KUTU 4
listem2 = ['Kahverengi', 'Kirmizi', 'Altin', "Gumus"]
kutu4 = Combobox(form, values=listem2)
kutu4.place(x=280, y=130, width =70)
#CALCULATE PART

###############
bant = {value:key for key,value in enumerate(listem)}

#5 BANTTT

liste = ['Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu5 = Combobox(form, values=liste)
kutu5.place(x=10, y=200, width =70)
#KUTU 5
listem = ['Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu6 = Combobox(form, values=listem)
kutu6.place(x=100, y=200, width =70)
#KUTU 6
kutu7 = Combobox(form, values=listem)
kutu7.place(x=190, y=200, width =70)
#KUTU 7
liste2 = ['Gumus',  'Altin', 'Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi']
kutu8 = Combobox(form, values=liste2)
kutu8.place(x=280, y=200, width =70)
#KUTU 8
listem2 = ['Kahverengi', 'Kirmizi', 'Altin', "Gumus"]
kutu9 = Combobox(form, values=listem2)
kutu9.place(x=370, y=200, width =70)
 # 6BANTTTTT

liste = ['Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu10 = Combobox(form, values=liste)
kutu10.place(x=10, y=300, width =60)
#KUTU 10
listem = ['Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi', 'Mor', 'Gri', 'Beyaz']
kutu11 = Combobox(form, values=listem)
kutu11.place(x=80, y=300, width =60)
#KUTU 11
kutu12 = Combobox(form, values=listem)
kutu12.place(x=150, y=300, width =60)
#KUTU 12
liste2 = ['Gumus',  'Altin', 'Siyah', 'Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Yesil', 'Mavi']
kutu13 = Combobox(form, values=liste2)
kutu13.place(x=230, y=300, width =60)
#KUTU 13
listem2 = ['Kahverengi', 'Kirmizi', 'Altin', "Gumus"]
kutu14 = Combobox(form, values=listem2)
kutu14.place(x=310, y=300, width =60)

kutu15 = Combobox(form, values=['Kahverengi', 'Kirmizi', 'Turuncu', 'Sari', 'Mavi', 'Mor'])
kutu15.place(x=380, y=300, width=60)


####################
carpan = {
'Gumus': 0.01,
'Altin':0.1,
'Siyah':1,
'Kahverengi':10,
'Kirmizi':100,
'Turuncu':1000,
'Sari':10000,
'Yesil':100000,
'Mavi':1000000
}
####################

tolerans = {'Kahverengi': 1,
            'Kirmizi': 2,
            'Altin': 5,
            "Gumus": 10
            }

sicaklik = {'Kahverengi': 100,
            'Kirmizi': 50,
            'Turuncu':15 ,
            'Sari': 25,
            'Mavi': 10 ,
            'Mor': 5 ,


}
########################

def hesapla():
    if len(kutu1.get())==0 or len(kutu2.get())==0 or len(kutu3.get())==0 or len(kutu4.get())==0:
        messagebox.askretrycancel(message='Lutfen renk secimini dogru yapiniz.')

    else:
        ohm = int(str(bant[kutu1.get()]) + str(bant[kutu2.get()])) * carpan[kutu3.get()]
        tole = str(tolerans[kutu4.get()])
        ilkdeger = str(bant[kutu1.get()]) + str(bant[kutu2.get()])
        ohmson = 'Ohm : ' + ilkdeger + ' ' + 'x' + ' ' + str(carpan[kutu3.get()]) + ' ' + '=' + ' ' + str(ohm) + ' ' + 'Ohm'
        toleson = 'Tolerans : ' + ' %' + tole
        dortlabel = Label(text=ohmson, bg='white')
        dortlabel.place(x=10, y=160)
        dortlabel2 = Label(text=toleson, bg='white')
        dortlabel2.place(x=10, y=180)
        ###

def hesapla2():
    if len(kutu5.get())==0 or len(kutu6.get())==0 or len(kutu7.get())==0 or len(kutu8.get())==0 or len(kutu9.get())==0:
        messagebox.askretrycancel(message='Lutfen renk secimini dogru yapiniz.')

    else:
        ohm2 = int(str(bant[kutu5.get()]) + str(bant[kutu6.get()]) + str(bant[kutu7.get()])) * carpan[kutu8.get()]
        tole2 = str(tolerans[kutu9.get()])
        ikincideger = str(bant[kutu5.get()]) + str(bant[kutu6.get()])
        ohmson2 = 'Ohm : ' + ikincideger + str(bant[kutu7.get()]) + ' ' + 'x' + ' ' + str(carpan[kutu8.get()]) + ' ' + '=' + ' ' + str(ohm2) + ' ' + 'Ohm'
        toleson2 = 'Tolerans : ' + ' %' + tole2
        dortlabel = Label(text=ohmson2, bg='white')
        dortlabel.place(x=10, y=240)
        dortlabel2 = Label(text=toleson2, bg='white')
        dortlabel2.place(x=10, y=260)
        ###

def hesapla3():
    if len(kutu10.get())==0 or len(kutu11.get())==0 or len(kutu12.get())==0 or len(kutu13.get())==0 or len(kutu14.get())==0:
        messagebox.askretrycancel(message='Lutfen renk secimini dogru yapiniz.')

    else:
        ohm2 = int(str(bant[kutu10.get()]) + str(bant[kutu11.get()]) + str(bant[kutu12.get()])) * carpan[kutu13.get()]
        tole2 = str(tolerans[kutu14.get()])
        ikincideger = str(bant[kutu10.get()]) + str(bant[kutu11.get()])
        ohmson2 = 'Ohm : ' + ikincideger + str(bant[kutu12.get()]) + ' ' + 'x' + ' ' + str(carpan[kutu13.get()]) + ' ' + '=' + ' ' + str(ohm2) + ' ' + 'Ohm'
        toleson2 = 'Tolerans : ' + ' %' + tole2
        sicaklikkat = 'Sicaklik Katsayisi : ' + str(sicaklik[kutu15.get()]) + ' ' + 'ppm/C'
        dortlabel3 = Label(text=ohmson2, bg='white')
        dortlabel3.place(x=10, y=320)
        dortlabel3 = Label(text=toleson2, bg='white')
        dortlabel3.place(x=10, y=340)
        dortlabel4 = Label(text=sicaklikkat, bg='white')
        dortlabel4.place(x=10, y=360)

        ###







dortbuton = Button(form, text="4 Hesapla", command = hesapla)
dortbuton.place (x =360 , y=125)      #BUTON KOORDINATI

besbuton =  Button(form, text="5 Hesapla", command = hesapla2)
besbuton.place (x =360 , y=235)

altibuton = Button(form, text="6 Hesapla", command = hesapla3)
altibuton.place (x =360 , y=345)


form.mainloop()

