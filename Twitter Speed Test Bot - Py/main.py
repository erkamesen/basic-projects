import time
from speedtest import Speedtest
from twitter import Twitter
import os
from dotenv import load_dotenv

load_dotenv() 

sp = Speedtest()
sp.openPage()
time.sleep(5)
sp.clicker(xp='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
#Site açıldı

time.sleep(50) #TESTING Süresi

infos = sp.getSpeedInfos()
print(infos)
sp.closeSpeedtest()
#############3
time.sleep(1)
mesaj = f"Download: {infos['download']} mpbs" \
        f"\nUpload: {infos['upload']} mpbs " \
        f"\nPing: {infos['Ping']} ms " \
        f"\nTeşekkürler {infos['ISS']} !!!! "

tw = Twitter(ID=os.getenv('ID'), password=os.getenv('PASSWORD'), msg=mesaj)
tw.openTw()
time.sleep(2)
tw.loginPart()
time.sleep(2)
tw.tweet()

