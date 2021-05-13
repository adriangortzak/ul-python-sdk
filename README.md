 <img src="https://www.ul.se/Static/gfx/ul-logo.jpg" width="200">

# About

Unofficial python client for travel information regarding [UL](https://ul.se).

For public transport around Uppsala.

[Notebook demo](https://colab.research.google.com/drive/115t8wyyuqVaT1R2dfN1xIFsAgspSls8S?usp=sharing)

# Installation

```python
pip3 install git+https://github.com/Adddrian/ul-api-python-client#egg=ul_api_client

```

# Usage

### import lib
```python
from ul_api_client import UlClient

```

### all_stops

Get a list of all stops

```python
UlClient.all_stops()
```

Response

```json
[
 {"id": 105005, "name": "Ekedal (Bro) (Upplands Bro)", "zon": "SLC", "lat": 59.583038494508415, "lng": 17.576156085725664, "chpriority": 0}, 
 {"id": 105112, "name": "Bålsta station (SL-pendeln) (Håbo)", "zon": "SLC", "lat": 59.56849714611362, "lng": 17.533543343754467, "chpriority": 3},
 ...
]
```

### stop_search

Search for a stop

```python
UlClient.stop_search("kantorsgatan")
```

Response

```json
[
    {
        "area": "",
        "coordinate": {
            "latitude": 59.874464131476444,
            "longitude": 17.641359295788952
        },
        "id": 700124,
        "name": "Kantorsgatan (Uppsala)",
        "type": 0
    },
    {
        "area": "",
        "coordinate": {
            "latitude": 59.87398469924595,
            "longitude": 17.64226147233132
        },
        "id": 37759,
        "name": "Kantorsgatan 2 Uppsala",
        "type": 1
    },
    ...
]
```

### journey_search

```python
UlClient.journey_search(700600, 700124)
```

Response

```json
[
    {
        "arrivalDateTime": "2021-05-13T08:57:00",
        "arrivalIsTimingPoint": false,
        "departureDateTime": "2021-05-13T08:42:00",
        "departureIsTimingPoint": true,
        "from": {
            "area": "A2",
            "coordinate": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "id": 700600,
            "name": "Uppsala Centralstation (Uppsala)",
            "type": 0
        },
        "hasRealTimeArrivalDeviation": true,
        "hasRealTimeDepartureDeviation": true,
        "journeyKey": "10229152424001100094700015500200021001100051300009700160019001200000000595008520857",
        "noOfChanges": 1,
        "priceZoneList": "7101",
        "realTimeArrivalDateTime": "2021-05-13T08:59:00",
        "realTimeDepartureDateTime": "2021-05-13T08:45:00",
        "routeLinks": [
            {
                "arrivalDateTime": "2021-05-13T08:43:00",
                "arrivalIsTimingPoint": false,
                "departureDateTime": "2021-05-13T08:42:00",
                "departureIsTimingPoint": true,
                "deviations": [],
                "from": {
                    "area": "A2",
                    "coordinate": {
                        "latitude": 0.0,
                        "longitude": 0.0
                    },
                    "id": 700600,
                    "name": "Uppsala Centralstation (Uppsala)",
                    "type": 0
                },
                "hasRealTimeArrivalDeviation": true,
                "hasRealTimeDepartureDeviation": true,
                "isCallTrip": false,
                "isCancelled": false,
                "line": {
                    "lineNo": 3,
                    "name": "3",
                    "towards": "Nyby",
                    "trafficType": 1,
                    "trainNo": 0
                },
                "notes": [],
                "path": [],
                "pointsOnRoute": [],
                "realTimeArrivalDateTime": "2021-05-13T08:46:00",
                "realTimeDepartureDateTime": "2021-05-13T08:45:00",
                "routeLinkKey": "10229152424001100094700015500200021",
                "to": {
                    "area": "L",
                    "coordinate": {
                        "latitude": 0.0,
                        "longitude": 0.0
                    },
                    "id": 700062,
                    "name": "Vaksala torg (Uppsala)",
                    "type": 0
                },
                "walkingDistance": null
            },
            ...
        ],
        "ticketType": {
            "additionalTicketTypes": null,
            "category": 0,
            "code": "UL1",
            "expires": "2021-05-20T08:51:16.7772887Z",
            "name": {
                "additions": null,
                "parts": [
                    {
                        "backgroundColor": "#f1c800",
                        "operator": "UL",
                        "text": "Zon 1",
                        "textColor": "#211b00"
                    }
                ]
            },
            "priceClasses": [
                {
                    "code": "VUL1",
                    "prices": [
                        {
                            "bellaTicketOfferIds": [
                                "3000"
                            ],
                            "type": 6,
                            "value": 3300
                        },
                        {
                            "bellaTicketOfferIds": [
                                "2995"
                            ],
                            "type": 3,
                            "value": 2700
                        },
                        {
                            "bellaTicketOfferIds": [
                                "2995"
                            ],
                            "type": 2,
                            "value": 2700
                        },
                        {
                            "bellaTicketOfferIds": [
                                "3000"
                            ],
                            "type": 0,
                            "value": 3300
                        }
                    ],
                    "type": 0
                },
                ...
            ],
            "validSeconds": 4500,
            "zones": [
                {
                    "backgroundColor": "#f1c800",
                    "code": "1",
                    "name": "Zon 1",
                    "network": "UL",
                    "textColor": "#211b00"
                }
            ]
        },
        "to": {
            "area": "",
            "coordinate": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "id": 700124,
            "name": "Kantorsgatan (Uppsala)",
            "type": 0
        },
        "travelTime": 14,
        "zones": [
            {
                "code": "1",
                "name": "UL zon 1",
                "network": "UL"
            }
        ]
    },
    ...
]
```


### journey_parts

```python
UlClient.journey_parts("10229152424001100051300009700160019")
```

Response


```json
{"journeyKey": "10229152424001100051300009700160019",
 "from": {"id": 700062,
  "name": "Vaksala torg (Uppsala)",
  "area": "L",
  "type": 0,
  "coordinate": {"latitude": 59.861522289371884,
   "longitude": 17.64553745728592}},
 "to": {"id": 700125,
  "name": "Djäknegatan (Uppsala)",
  "area": "B",
  "type": 0,
  "coordinate": {"latitude": 59.87185368253636,
   "longitude": 17.639269053062165}},
 "departureDateTime": "2021-05-13T06:49:00Z",
 "departureIsTimingPoint": false,
 "hasRealTimeDepartureDeviation": false,
 "realTimeDepartureDateTime": null,
 "arrivalDateTime": "2021-05-13T06:52:00Z",
 "arrivalIsTimingPoint": false,
 "hasRealTimeArrivalDeviation": false,
 "realTimeArrivalDateTime": null,
 "travelTime": 3,
 "routeLinks": [{"routeLinkKey": "10229152424001100051300009700160019",
   "line": {"name": "2",
    "lineNo": 2,
    "trainNo": 0,
    "towards": "Gamla Uppsala",
    "trafficType": 1},
   "to": {"id": 700125,
    "name": "Djäknegatan (Uppsala)",
    "area": "B",
    "type": 0,
    "coordinate": {"latitude": 59.87185368253636,
     "longitude": 17.639269053062165}},
   "from": {"id": 700062,
    "name": "Vaksala torg (Uppsala)",
    "area": "L",
    "type": 0,
    "coordinate": {"latitude": 59.861522289371884,
     "longitude": 17.64553745728592}},
   "departureDateTime": "2021-05-13T06:49:00Z",
   "departureIsTimingPoint": false,
   "hasRealTimeDepartureDeviation": false,
   "realTimeDepartureDateTime": null,
   "arrivalDateTime": "2021-05-13T06:52:00Z",
   "arrivalIsTimingPoint": false,
   "hasRealTimeArrivalDeviation": false,
   "realTimeArrivalDateTime": null,
   "walkingDistance": null,
   "isCallTrip": false,
   "isCancelled": false,
   "notes": [],
   "pointsOnRoute": [{"id": 700581,
     "name": "Väderkvarnsgatan (Uppsala)",
     "area": "B",
     "arrivalDateTime": "2021-05-13T06:50:00Z",
     "arrivalIsTimingPoint": false,
     "hasRealTimeArrivalDeviation": true,
     "realTimeArrivalDateTime": "2021-05-13T06:52:00Z",
     "coordinate": {"latitude": 59.865157812561,
      "longitude": 17.642364004831975}},
    {"id": 700126,
     "name": "Portalgatan (Uppsala)",
     "area": "B",
     "arrivalDateTime": "2021-05-13T06:51:00Z",
     "arrivalIsTimingPoint": false,
     "hasRealTimeArrivalDeviation": true,
     "realTimeArrivalDateTime": "2021-05-13T06:53:00Z",
     "coordinate": {"latitude": 59.86830136561798,
      "longitude": 17.639698431337212}}],
   "path": [{"latitude": 59.861522289371884, "longitude": 17.64553745728592},
    {"latitude": 59.86156168013393, "longitude": 17.6454812592386},
    {"latitude": 59.86173847811869, "longitude": 17.64586553920738},
    {"latitude": 59.861749455375346, "longitude": 17.645889530518343},
    {"latitude": 59.862319860058236, "longitude": 17.647172602495516},
    {"latitude": 59.87185368253636, "longitude": 17.639269053062165},
    ...],
   "deviations": []}],
 "priceZoneList": "7101",
 "ticketType": {"code": "UL1",
  "category": 0,
  "name": {"parts": [{"operator": "UL",
     "backgroundColor": "#f1c800",
     "textColor": "#211b00",
     "text": "Zon 1"}],
   "additions": null},
  "zones": [{"network": "UL",
    "code": "1",
    "name": "Zon 1",
    "backgroundColor": "#f1c800",
    "textColor": "#211b00"}],
  "validSeconds": 4500,
  "priceClasses": [{"type": 0,
    "code": "VUL1",
    "prices": [{"type": 6, "value": 3300, "bellaTicketOfferIds": ["3000"]},
     {"type": 3, "value": 2700, "bellaTicketOfferIds": ["2995"]},
     {"type": 2, "value": 2700, "bellaTicketOfferIds": ["2995"]},
     {"type": 0, "value": 3300, "bellaTicketOfferIds": ["3000"]}]},
   {"type": 1,
    "code": "UUL1",
    "prices": [{"type": 6, "value": 2000, "bellaTicketOfferIds": ["3031"]},
     {"type": 3, "value": 1700, "bellaTicketOfferIds": ["3009"]},
     {"type": 2, "value": 1700, "bellaTicketOfferIds": ["3009"]},
     {"type": 0, "value": 2000, "bellaTicketOfferIds": ["3031"]}]}],
  "expires": "2021-05-20T08:51:16.7772887Z",
  "additionalTicketTypes": null},
 "noOfChanges": 0,
 "zones": [{"network": "UL", "code": "1", "name": "UL zon 1"}]}
```
