#import requests

#url = "https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/search"

#querystring = {"location":"Brownsville, TX","page":"1","sort_by":"Newest"}

#headers = {
    #"X-RapidAPI-Key": "cfdb68d422msh4947d1dac059640p1ac971jsn5033c0913dc3",
        #"X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
#}

#response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

#import requests

#url = "https://realty-in-us.p.rapidapi.com/properties/v3/list"

#payload = {
    #"limit": 200,
    #"offset": 100,
    #"postal_code": "90004",
#}
#headers = {
    #"content-type": "application/json",
        #"X-RapidAPI-Key": "cfdb68d422msh4947d1dac059640p1ac971jsn5033c0913dc3",
        #"X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
#}

#response = requests.post(url, json=payload, headers=headers)
#res = response.json()
#idx = 0
#for i in res['data']['home_search']['results']:
    #idx += 1
    #print(idx, " : ", i['property_id'], i['status'])
    
    

#import requests

#url = "https://realty-in-us.p.rapidapi.com/agents/list"

#querystring = {"postal_code":"11234","offset":"0","limit":"20","sort":"recent_activity_high","types":"agent"}

#headers = {
    #"X-RapidAPI-Key": "cfdb68d422msh4947d1dac059640p1ac971jsn5033c0913dc3",
        #"X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
#}

#response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

import requests
from datetime import datetime

url = "https://redfin-com-data.p.rapidapi.com/property/search"

querystring = {"location":"Austin","sort":"Newest"}

headers = {
    "X-RapidAPI-Key": "cfdb68d422msh4947d1dac059640p1ac971jsn5033c0913dc3",
        "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


res= response.json()
idx = 0
for i in res['data']['homes']:
    idx += 1
    if "soldDate" in i:
        dt = datetime.fromtimestamp(int(i['soldDate'])/1000)
        print(idx, " : ", dt)