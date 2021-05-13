import requests
import json




def all_stops():
    url = "https://www.ul.se/api/journey/allstops"
    return requests.request("GET", url).json()


def stop_search(search_query):
    search_result_json = requests.get("https://www.ul.se/api/journey/stops?query=" + search_query).json()
    search_result_df_raw = []
    for row in search_result_json:
        search_result_df_raw.append(flatten_json(row))
    return search_result_df_raw


def journey_search(from_point_id, from_point_type, to_point_id, to_point_type, max_walk_distance=3000):
    journey_search_reply = json.loads(requests.get("https://www.ul.se/api/journey/search?changeTimeType=0&dateTime=&fromPointId=" + str(from_point_id) + "&fromPointType=" + str(from_point_type) + "&maxWalkDistance=" + str(max_walk_distance) + "&priorityType=0&toPointId=" + str(to_point_id) + "&toPointType=" + str(to_point_type) + "&trafficTypes=1,2,3,4,5,6,7,8,9,10,11&travelWhenType=2&via=&viaPointId=&walkSpeedType=0").json()['Payload'])[0]
    return journey_search_reply


def journey_parts(route_link_key):
    return requests.get("https://www.ul.se/api/journey/parts/?journeyKey=" + route_link_key).json()








# Help functions

def flatten_json(y):
    out = {}
  
    def flatten(x, name =''):
          
        # If the Nested key-value 
        # pair is of dict type
        if type(x) is dict:
              
            for a in x:
                flatten(x[a], name + a + '_')
                  
        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:
              
            i = 0
              
            for a in x:                
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
  
    flatten(y)
    return out
