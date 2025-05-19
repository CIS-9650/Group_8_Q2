# This code was written to make sure that the geolocation sub-routine that
# was designed to return the latitude and longitude for the cities on our 
# universities list, actually returned the correct values. 

# Since there may be several cities in the US that share a name, this code uses 
# the same list of college cities as our main solution to question #2, as well as
# the same function to determine lat and long for these as in our main solution. 

# This script then takes the lat and long values and reverse locates them to 
# return city, state, and country. 

# The state data revealed that the correct city was being geolocated by the 
# latlong function.

from geopy.geocoders import Nominatim
import time

def latlong(city):
  geolocator = Nominatim(user_agent="CIS9650")
  location = geolocator.geocode(city)
  lat = location.latitude
  lon = location.longitude
  loc = f'{lat}, {lon}'
  return (loc)
  
def reverse_geocode(coord):
  geolocator = Nominatim(user_agent="CIS9650")
  location = geolocator.reverse(coord, exactly_one=True)
  address = location.raw['address']
  city = address.get('city', '')
  state = address.get('state', '')
  country = address.get('country', '')
  return city, state, country


places = [
    'New York', 'Paris', 'London', 'Los Angeles','Lincoln',"Cambridge",
    "Stanford","Pasadena","Philadelphia","Berkeley","Ithaca","Chicago",     
    "Princeton","New Haven","Baltimore","New York City","Los Angeles",
    "New York City","Ann Arbor","Evanston","Pittsburgh","Durham","Austin",
    "Champaign","San Diego","Seattle","Providence","University Park",
    "West Lafayette","Boston","Atlanta","Madison"
        ]

for place in places:
  location = f'{place}, USA'
  loc = latlong(location)
  time.sleep(1)
  city,state,country = reverse_geocode(str(loc))
  print (f'City from university list: {place}')
  print (f'lat & long from function: {loc}')
  print (f'Return value from reverse lookup: {city,state,country}\n')
  time.sleep(1)
