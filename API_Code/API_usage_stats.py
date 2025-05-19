# Code returns the API usage stats and requests remaining for a given timeframe.
# Keeping track helps to avoid running into rate limits.

url = 'https://api.weatherbit.io/v2.0/subscription/usage?key=ff690c5a1b744d609b637aa8f66e6114'
response = requests.get(url)
if response.status_code == 200:
  
  data = response.json()         # data returns 'dashboard' info on API usage
  
  pretty_json = json.dumps(data, indent=4)
  print(pretty_json)
else:
  print (f'the request failed (error {response.status_code})')