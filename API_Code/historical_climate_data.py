import requests
import json
import pandas as pd
from geopy.geocoders import Nominatim
import time


cities = ['New York', 'Paris', 'London', 'Los Angeles']


def getInfo(lat,lon,start_day,end_day):
  url = f'https://api.weatherbit.io/v2.0/normals?lat={lat}&lon={lon}&start_day={start_day}&end_day={end_day}&units=I&tp=monthly&key=ff690c5a1b744d609b637aa8f66e6114'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print (f'the request failed (error {response.status_code})')


def latlong(city):
  geolocator = Nominatim(user_agent="CIS9650")
  location = geolocator.geocode(city)
  lat = location.latitude
  lon = location.longitude
  loc = str(lat), str(lon)
  return (loc)


def get_season(start_day, end_day):
  temp_list=[]
  for city in cities:
    location = latlong(city)
    time.sleep (1)
    weather = getInfo(location[0],location[1],start_day,end_day)
    season = (weather["data"])

    #pretty_json = json.dumps(weather, indent=4)
    #print(pretty_json)
    #print (season)

    total = 0
    for month in season:
      total += (month['temp'])
    avg_temp = round(total / len(season),1)
    temp_list.append (avg_temp)

  dict = {
    'city':cities,
    'Avg Temp':temp_list
        } 
  return dict


tri_one = get_season('09-01','12-31')
df1 = pd.DataFrame(tri_one)
print(df1)

tri_two = get_season('01-01','03-31')
df2 = pd.DataFrame(tri_two)
print(df2)

tri_three = get_season('04-01','06-30')
df3 = pd.DataFrame(tri_three)
print(df3)
