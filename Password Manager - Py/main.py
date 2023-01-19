from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json



# ----------------------------  SEARCH  ------------------------------- #

def seek():
    try:
        with open("registerinfos.json", "r") as __:
            dxata = json.load(__)
            aranicak = dxata[website_entry.get()]
            yazi = f"email: {aranicak['email']}\npassword: {aranicak['Password']}"
            messagebox.showinfo(title="Found", message=yazi)
    except:
        messagebox.showinfo(title="Not found", message="No data file found.")


# ---------------------------- READ  ------------------------------- #

def read():
    toplevel = Toplevel()
    toplevel.title("INFO")
    toplevel.geometry("800x800")
    toplevel.config(bg="#FAD6A5")
    readlabel = Label(toplevel,bg="#FAD6A5")
    with open("registerinfos.json", "r") as f:
        yazi = f.read()

    readlabel.config(text=yazi)
    readlabel.pack()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
            # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg="#FAD6A5", padx=50, pady=50, highlightthickness=0)
window.title("Password Manager")

# CANVAS
canvas = Canvas(height=200, width=200,bg="#FAD6A5", highlightthickness=0)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0)



# LABELS
website_label = Label(window, text="Website:",bg="#FAD6A5",fg="#E0144C")
website_label.grid(column=0, row=1 )

username_label = Label(window, text="Email/Username:",bg="#FAD6A5",fg="#E0144C")
username_label.grid(column=0, row=2 )

password_label = Label(window, text="Password:",bg="#FAD6A5",fg="#E0144C")
password_label.grid(column=0, row=3 )

# ENTRYS

website_entry = Entry(window,width=26, bg="#CFB997")
website_entry.grid(column=1, row=1)
website_entry.focus()
username_entry = Entry(window, width=35,bg="#CFB997")
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "erkamesen789@gmail.com")
password_entry = Entry(window, width=26,bg="#CFB997")
password_entry.grid(column=1, row=3)

# BUTTONS

generate = Button(window, text="Generate",bg="#9BA17B",activebackground="#E0144C", command=generatepass)
generate.grid(column=2, row=3)

add = Button(window, text="Add", width=36,bg="#9BA17B",activebackground="#E0144C", command=addinfos)
add.grid(column=1, row=4, columnspan=2)

reading = Button(window, text="Read", width=1,bg="#61764B",activebackground="#E0144C", command=read)
reading.grid(column=0, row=0)

search = Button(window, text="Search",width=7, bg="#9BA17B",activebackground="#E0144C", command=seek)
search.grid(column=2, row=1)



window.mainloop()


