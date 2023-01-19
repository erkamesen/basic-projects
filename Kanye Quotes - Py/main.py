from tkinter import *
import requests
from googletrans import Translator
url = "https://api.kanye.rest/"

translator = Translator()
def get_quote():
    global quote_text
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    yazi = translator.translate(data["quote"], dest="tr")
    canvas.itemconfig(quote_text, text=yazi.text)

window = Tk()
window.title("Kanye Says... ")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
resim = PhotoImage(file="background.png")
canvas.create_image(150, 207, image = resim)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE",
                                width=250, font=("Arial", 20, "italic"), fill="white")
canvas.grid(column=0, row=0, columnspan=2)


resim2 = PhotoImage(file="kanye.png")

buton=Button(image=resim2, command= get_quote, highlightthickness=0)
buton.grid(column =0, row=1, columnspan=2)


window.mainloop()