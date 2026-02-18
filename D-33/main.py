import requests

MY_LAT = 12.971599
MY_LONG = 77.594566

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()
print(data['iss_position'])




parameters = {
   "lat": MY_LAT,
   "lng": MY_LONG,
   "formatted": 0
}
response_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_sunset.raise_for_status()
data_sunset = response_sunset.json()
print(data_sunset['results']['sunset'])