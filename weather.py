import requests
import pp
import datetime

city = input("Enter the city:")
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7f942b5c9115843184a274294cb88783&units=matrics'.format(city)
res = requests.get(url)
data = res.json()

x = datetime.datetime.now()
d = int(x.strftime("%d"))

print(d)
timezone = data['timezone']
print('Timezone:{}'.format(timezone))

if d > 1:
   for i in range(2,d):
       if (d % i) == 0:
           print(d,"Date is not a prime so no date")
           break
   else:
       print(d,"Date is a prime number")
       pp(data)
else:
   print(d,"Date is not a prime so no date")
