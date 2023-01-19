from tkinter import *


screen = Tk()
screen.config(bg="dark salmon",padx=20,pady=20)
screen.title("Mile to Km Converter")



input = Entry(width=5, font=20,bg="pale violet red")
input.grid(column=1, row=0)
label = Label(text="Miles", font= "Times 14 bold", bg="dark salmon", fg="white")
label.grid(column=2, row=0)

isequal = Label(text="is equal to", bg="dark salmon", fg="white",font= "Times 14 bold")
isequal.grid(column=0,row=1)
def sonuc():
    sonuclabel.config(text=round(int(input.get())*1.60934, 1))

sonuclabel=Label(text="0", bg="dark salmon", fg="white",font= "Times 14 bold")
sonuclabel.grid(column=1,row=1)



km = Label(text="Km",bg="dark salmon", fg="white",font= "Times 14 bold")
km.grid(column=2,row=1)

buton = Button(text="Calculate",bg="dark salmon", fg="white",font= "Times 14 bold",
               activebackground="firebrick", command=sonuc)
buton.grid(column=1, row=2)


screen.mainloop()