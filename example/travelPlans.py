import ul_api
import re
import datetime
import pytz


def addtwohour(editTime):
 timeOb = datetime.datetime.strptime(editTime,'%H:%M')
 return '{:%H:%M}'.format(timeOb + datetime.timedelta(hours=2))

get_time = re.compile('\d{2}[:]\d{2}')

print ('---Buss information---')
print ('Från Akademiska sjukhuset södra til Uppsala C')
print ('Beräkningar från ' + datetime.datetime.now(pytz.timezone('Europe/Stockholm')).strftime('%Y-%m-%d  %H:%M'))
print ('----------------------')
print ('\n')
count=0

obj=ul_api.getTravelInfoNowJson(700025, 700600)

for i in obj:
 count = count + 1
 print ('-------- Alternativ ' + str(count) +  ' --------')
 print(addtwohour(get_time.findall(i['departureDateTime'])[0]) + ' - ' + addtwohour(get_time.findall(i['arrivalDateTime'])[0]))
 for p in  i['routeLinks']:
  print ('(' + addtwohour(get_time.findall(p['departureDateTime'])[0])  + ') ' +p['line']['name'] + ' -mot-> ' +  p['line']['towards'])
 print ('\n')
print ('------------------------------')

