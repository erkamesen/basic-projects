from tkinter import *
import random

import csv

##########
with open("/home/erkam/deneme/kelimeler.txt") as f:
    kelimelistesi = []
    sa = f.readlines()
    for a,x in enumerate(sa):
        y = x.split("\t")
        y.remove(y[0])
        kelimelistesi.append(y)
engwords = []
trwords = []
for kelime in kelimelistesi:
    ingword = kelime[0]
    engwords.append(ingword)
    kelime.remove(ingword)
    trwords.append(kelime[0].replace("\n", ""))
wordicteng = dict(zip(engwords, trwords))
wordicttr = dict(zip(trwords, engwords))
###########

# # # # # # # # # # # # # # # # # # # # # # # #


"""
worddicttr - Turkish to English - type = Dict

worddicteng - English to Turkish - type = Dict

engwords - English words - type = List

trwords - Turkish words - type = List
"""
# # # # # # # # # # # # # # # # # # # # # # # #

BACKGROUND_COLOR = "#B1DDC6"
TITLEFONT = ("Ariel", 40, "italic")
WORDFONT = ("Ariel", 40, "bold")

to_learn={}


def next_card():
    global current_word, flip_timer, nd
    kelime=random.choice(trwords)
    current_word = wordicttr[kelime]
    if kelime in to_learn:
        next_card()
    else:
        nd = {kelime:current_word}
        window.after_cancel(flip_timer)
        canvas.itemconfig(card_background, image=card_front_img)
        canvas.itemconfig(card_title, text="Turkish", fill="black")
        canvas.itemconfig(card_word, text=kelime, fill="black")
        flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word)

def is_known():
    with open("to_learn.csv") as data_learn:
        deneme = csv.DictReader(data_learn)
        print(deneme)
        if kelime not in deneme:
            with open("to_learn.csv", "a", encoding="UTF-8") as f:
                to_learn.update(nd)
                for key,value in to_learn.items():
                    f.write(f"{key},{value}\n")
                to_learn.clear()


    next_card()






#####################################################3


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img =  PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=TITLEFONT)
card_word =canvas.create_text(400, 263, text="", font=WORDFONT)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image=PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()




