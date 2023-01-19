import datetime as dt


now = dt.datetime.now()
print(now)
#result = 2022-10-29 11:30:46.178089
year = now.year
print(year)
#result = 2022 type(int)
month = now.month
print(month)
#result = 10 type(int)
day_of_week = now.weekday()
print(day_of_week)
#result = Monday == 0 and each day +=1

date_of_birth = dt.datetime(year=1994,month=10,day=25, hour=13) #datetime classı attribute ları
print(date_of_birth)
#result = 1994-10-25 13:00:00 HOUR YAZILMASADA OLUR Y M D ZORUNLU



