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