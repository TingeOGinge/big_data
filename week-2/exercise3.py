import requests

keyAPI = '9f418d12e2c0f5e721197b55a91010a3'
city = 'Portsmouth'
country = 'uk'
urlAPI = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={keyAPI}"

req = requests.get(urlAPI)
data = None
try:
  data = req.json()
except ValueError as err:
  print(f"JSON Parsing failed: \n {err}")

def kelvinToCelsius(temp):
  return temp - 273.15

if data is not None:
  print(
    f"City: {data['name']} \n" +
    f"Weather: {data['weather'][0]['description']} \n" +
    f"Temperature (in Kelvin): {data['main']['temp']:.2f} \n" +
    f"Temperature (in Celsius): {kelvinToCelsius(data['main']['temp']):.2f} \n" +
    f"Wind speed: {data['wind']['speed']} \n"
  )