import requests
def get(distance):
    coord = set()
    url = "https://api.foursquare.com/v3/places/search?ll=28.6347%2C77.3046&radius="+str(distance)+"&categories=12094&limit=50"
    headers = {
        "accept": "application/json",
        "Authorization": "[Get yours from README]"
    }
    response = requests.request("GET",url, headers=headers)
    resp = response.json()
    for x in resp['results'] :
        #temp['lat'].append(x['geocodes']['main']['latitude'])
        #temp['lon'].append(x['geocodes']['main']['longitude'])
        coord.add((x['geocodes']['main']['latitude'],x['geocodes']['main']['longitude'],x['name']))
    return coord

req_cat = {'Restaurant':13065,'Fruit and Vegetable':17067,'Grocery Store':17069,
           'Health and Medicine':15000,'Sweets and Snacks':13210,'Metro Station':19046}

def get_cat(x,y,category):
    url = "https://api.foursquare.com/v3/places/search?ll="+str(x)+"%2C"+str(y)+"&radius=1000&categories="+str(category)+"&limit=50"
    headers = {
        "accept": "application/json",
        "Authorization": "[Get Yours from README]"
    }
    response = requests.request("GET",url,headers=headers)
    resp = response.json()
    return len(resp['results'])
