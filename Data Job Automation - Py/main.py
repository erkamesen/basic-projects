from zillow import Zillow
from dataautomation import Dataenter
import time

# zillow -> getPrices -> list
# zillow -> getLinks -> list
# zillow -> getAddress -> list


zl = Zillow()
tosheet = Dataenter()


prices = zl.getPrices()
links = zl.getLinks()
addresses = zl.getAddress()

tosheet.openPage()
time.sleep(3)
for _ in range(len(prices)):
    time.sleep(2)
    tosheet.inputPart(link=links[_],price=prices[_], address=addresses[_])

tosheet.closePage()



