from pytube import YouTube


URL = YouTube(url="https://www.youtube.com/watch?v=mZwBZ9KRux4")

print(URL.rating)