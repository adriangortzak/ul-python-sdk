import requests
import json
import datetime
import pytz
from io import BytesIO
import pycurl
import re

def addtwohour(editTime):
 timeOb = datetime.datetime.strptime(editTime,'%H:%M')
 return '{:%H:%M}'.format(timeOb + datetime.timedelta(hours=2))



now = datetime.datetime.now(pytz.timezone('Africa/Monrovia'))

date = now.strftime('%Y-%m-%d')
time = now.time().strftime('%H:%M')

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.ul.se/api/v2/journeys/?fromPointId=700025&fromPointType=0&toPointId=700600&toPointType=0&dateTime=' + date + 'T' + time + ':00.000Z&directionType=0')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
obj = json.loads(body.decode('utf-8'))

get_time = re.compile('\d{2}[:]\d{2}')

print ('---------------Buss information--------------')
print ('Från Akademiska sjukhuset södra til Uppsala C')
print ('Beräkningar från ' + datetime.datetime.now().strftime('%Y-%m-%d  %H:%M'))
print ('---------------------------------------------')
print ('\n')
count=0

for i in obj:
 count = count + 1
 print ('-------- Alternativ ' + str(count) +  ' --------')
 print(addtwohour(get_time.findall(i['departureDateTime'])[0]) + ' - ' + addtwohour(get_time.findall(i['arrivalDateTime'])[0]))
 for p in  i['routeLinks']:
  print ('(' + addtwohour(get_time.findall(p['departureDateTime'])[0])  + ') ' +p['line']['name'] + ' -mot-> ' +  p['line']['towards'])
 print ('\n')
print ('------------------------------')

