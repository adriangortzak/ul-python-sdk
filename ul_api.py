#################################################################
#								#
#								#
#								#
#################################################################

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


def getTravelInfoNowJson(fromStationID, toStationID):
 now = datetime.datetime.now(pytz.timezone('Europe/Stockholm'))

 date = now.strftime('%Y-%m-%d')
 time = now.time().strftime('%H:%M')

 buffer = BytesIO()
 c = pycurl.Curl()
 c.setopt(c.URL, 'https://api.ul.se/api/v2/journeys/?fromPointId='+str(fromStationID)+'&fromPointType=0&toPointId='+str(toStationID)+'&toPointType=0&dateTime=' + date + 'T' + time + ':00.000Z&directionType=0')
 c.setopt(c.WRITEDATA, buffer)
 c.perform()
 c.close()

 body = buffer.getvalue()
 obj = json.loads(body.decode('utf-8'))
 return obj

def getTravelInfoNowJson(fromStationID, toStationID, date, time):

 buffer = BytesIO()
 c = pycurl.Curl()
 c.setopt(c.URL, 'https://api.ul.se/api/v2/journeys/?fromPointId='+str(fromStationID)+'&fromPointType=0&toPointId='+str(toStationID)+'&toPointType=0&dateTime=' + date + 'T' + time + ':00.000Z&directionType=0')
 c.setopt(c.WRITEDATA, buffer)
 c.perform()
 c.close()

 body = buffer.getvalue()
 obj = json.loads(body.decode('utf-8'))
 return obj






def searchBusStationJson(name):
 buffer = BytesIO()
 c = pycurl.Curl()
 c.setopt(c.URL, 'https://api.ul.se/api/v2/stops/?query=' + name)
 c.setopt(c.WRITEDATA, buffer)
 c.perform()
 c.close()
 body = buffer.getvalue()
 obj = json.loads(body.decode('utf-8'))
 print(obj)

