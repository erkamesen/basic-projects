from tkinter import *
from tkinter import messagebox
from pytube import YouTube

class Ekran():

    def __init__(self):
        self.window = Tk()
        self.window.config(bg="navajo white",pady=50,padx=20)
        self.window.title("YouTube Downloader")
        self.window.wm_minsize(width=540, height=800)
        resim = PhotoImage(file="ytlogo2.png")
        self.canvas = Canvas(self.window,width=480,height=480, highlightthickness=0, background="navajo white")
        ytlogo = self.canvas.create_image(240,240, image=resim)
        self.canvas.grid(row=1, column=0, columnspan=2)
        audiologo = PhotoImage(file="audiologo.png")
        videologo = PhotoImage(file="videologo.png")
        self.inputentry= Entry()
        self.inputentry.config(width=40)
        self.inputentry.grid(row=0, column=0, columnspan=2)
        self.buton1 = Button(image=audiologo,highlightthickness=0,
                             bg="navajo white",
                             activebackground="navajo white", command=self.audiodownload)
        self.buton2 = Button(image=videologo,highlightthickness=0,
                             bg="navajo white",
                             activebackground="navajo white", command=self.videodownload)
        self.buton1.grid(row=2, column=0)
        self.buton2.grid(row=2, column=1)


        self.window.mainloop()

    def videodownload(self):
        self.videodownloader = YouTube(self.inputentry.get())
        indir = self.videodownloader.streams.filter(progressive=True, resolution="720p").first()
        indir.download(output_path="/home/erkam/Downloads/YTDownloader")
        self.inputentry.delete(0, END)
        messagebox.showinfo(title="!!!", message="Başarılı Şekilde İndirildi")

    def audiodownload(self):
        self.audiodownloader = YouTube(self.inputentry.get())
        indir = self.audiodownloader.streams.filter(mime_type="audio/mp4").first()
        indir.download(output_path="/home/erkam/Downloads/YTDownloader")
        self.inputentry.delete(0, END)
        messagebox.showinfo(title="!!!", message="Başarılı Şekilde İndirildi")







