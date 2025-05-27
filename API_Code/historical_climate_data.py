# historical_climate_data.py

# The code below makes an API request to www.weatherbit.io to retreive historical 
# climate data for unique locations. The data being queried here is based on average 
# temperatures, precipitation, and snowfall for a given month based on data 
# collected between 1991 and 2020. 

# Once the data is retreived, this script then takes the average temperatures for 
# each trimester of the college year (Fall = Sept-December, Winter = January-March,
# Spring = April-June). The script also returns the total precipitation and snowfall
# for the entire school year.

import requests
import json
import pandas as pd
from geopy.geocoders import Nominatim
import time

# Vivek:

  # The name of the cities from Riya's web scrape needs to be the source for the list 
  # named 'cities' below.  Currently this is just a sample list for the pupose of 
  # testing this code.

  # Since the scrape only includes US schools, I have already accounted for the country
  # in the API call, so only the name of the city is needed for the list.

  # Only the first 30 universities should be returned in order to avoid running into
  # rate limit issues during the API call.

cities = ['New York', 'Paris', 'London', 'Los Angeles']


# getInfo is the function call that returns the historical climate data for a 
# particular location in latitude and longitude. 

# Vivek: 

  # Currently this is a static set of json data similar to what the API would return.
  # In order to avoid network issues and problems with API rate limiting, this code 
  # employs this sample data rather than real return data. As a result, all the cities 
  # in the list from the scrape will share the exact same data. Ignore this for now,
  # since this data will be sufficient for testing any code built on this one. 
  # We can replace this with the lines of code for the API call, when the final
  # python file is running fully. 
  
  # The actual API-call code is below this test function (and commented out).

def getInfo(lat,lon):
  data = {
             "lat":35.5,
             "lon":-75.5,
             "timezone":"America\/New_York",
             "sources":[
                "era5"
              ],
              "data":[{
                         "dewpt":6.8,
                         "snow":0,
                         "min_wind_spd":0.4,
                         "wind_dir":269,
                         "hour":5,
                         "month":1,
                         "max_temp":13.4,
                         "day":2,
                         "wind_spd":1.4,
                         "temp":11.2,
                         "min_temp":9.4,
                         "max_wind_spd":2.4,
                         "precip":5.32
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":2,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":3,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":4,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":5,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":6,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":7,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":8,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":9,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":10,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":11,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                },
                {
                         "dewpt":6,
                         "snow":0.6,
                         "min_wind_spd":1.6,
                         "wind_dir":270,
                         "hour":5,
                         "month":12,
                         "max_temp":13,
                         "day":3,
                         "wind_spd":2.1,
                         "temp":10.5,
                         "min_temp":8.6,
                         "max_wind_spd":2.8,
                         "precip":2.85
                      
                }
              ]
        }
  return data

# this is the actual getInfo function to pull data from the API. To be uncommmented
# once this final python code has been merged and debugged. This will prevent running
# out of API requests.

#def getInfo(lat,lon):
#  url = f'https://api.weatherbit.io/v2.0/normals?lat={lat}&lon={lon}&start_day=01-01&end_day=12-31&units=I&tp=monthly&key=API_KEY'
#  response = requests.get(url)
#  if response.status_code == 200:
#    data = response.json()
#    return data
#  else:
#    print (f'the request failed (error {response.status_code})')



# Since the API will only return historical climate data based on the latitude
# and longitude of one of our cities in the list, latlong is the function call 
# that translates our list of cities into a usable geolocation point.

def latlong(city):
  geolocator = Nominatim(user_agent="CIS9650")
  location = geolocator.geocode(city)
  lat = location.latitude
  lon = location.longitude
  loc = str(lat), str(lon)
  return (loc)


# get_season is the funtion that processes the raw historical climate data 
# for the final table of data.

def get_season(season):
  temp_list=[]    #lists where month-on-month weather point data are assembled
  rain_list=[]
  snow_list=[]

  for city in cities:
    location = latlong(f'{city},USA') # USA added to each city to ensure correct geolocation
    time.sleep (1)  # a little delay to avoid making too many requests per second
    weather = getInfo(location[0],location[1])  # the raw json data
    year = (weather["data"])  # the relevant json data returned by the API

    total_temp = 0
    total_snow = 0
    total_rain = 0
    for month in year:
      if month['month'] in season:  # ensures function returns values for correct trimester months
        total_temp += (month['temp'])
        total_snow += (month['snow'])
        total_rain += (month['precip'])
      else: continue

    avg_temp = round(total_temp / len(season),1) # calculates average temp for trimester

    temp_list.append (avg_temp)
    snow_list.append (total_snow)  # collecting total rain and snow per trimester
    rain_list.append (total_rain)  # trimester data summed in the dataframe to reduce API calls

  dict = {      # dictionary of lists to build the dataframe for each trimester
    'City':cities,
    'Avg Temp':temp_list,
    'Total Rain':rain_list,
    'Total Snow':snow_list
        }
  return dict



# MAIN #

tri_one = get_season([9,10,11,12])  # pulls climate data for sep (9) - dec (12)
df1 = pd.DataFrame(tri_one)

tri_two = get_season([1,2,3])
df2 = pd.DataFrame(tri_two)

tri_three = get_season([4,5,6])
df3 = pd.DataFrame(tri_three)


print('School Year Historical Climate Data by Trimester')
print('------------------------------------------------')

# dataframes for the three trimesters are combined here based on City
merged_df = pd.merge(df1, df2, on='City', how='left')
all_merge = pd.merge(merged_df, df3, on='City', how='left')

# columns renamed to make display of dataframe meaningfull
all_merge = all_merge.rename(columns={
    'Avg Temp_x':'T1 Avg Temp','Total Rain_x':'T1 Rain','Total Snow_x':'T1 Snow',
    'Avg Temp_y':'T2 Avg Temp','Total Rain_y':'T2 Rain','Total Snow_y':'T2 Snow',
    'Avg Temp':'T3 Avg Temp','Total Rain':'T3 Rain','Total Snow':'T3 Snow'
    })

# rain and snow from the three dataframes are added together here:
all_merge['Total SY Snow'] = round(all_merge[['T1 Snow','T2 Snow','T3 Snow']].sum(axis=1),1)
all_merge['Total SY Rain'] = round(all_merge[['T1 Rain','T2 Rain','T3 Rain']].sum(axis=1),1)

# since total snow and rain data for the whole year is all that is required,
# the columns with the trimester totals for rain and snow are removed from final display.
final_table = all_merge.drop(columns=['T1 Snow','T2 Snow','T3 Snow','T1 Rain','T2 Rain','T3 Rain'])


# final_table is the dataframe ready to be saved as a csv and database
display(final_table)

