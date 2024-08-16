import requests

def get_weather(api_key, city_name):
  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"


  response = requests.get(complete_url)

  weather_data = response.json()

  print(weather_data)

  if weather_data['cod'] == 200:
    main = weather_data['main']
    weather = weather_data['weather'][0]

    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_description = weather["description"]

    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_description}")
  else:
      print("City not found. Please check the city name and try again.")

if __name__ == "__main__":
    api_key = '6a1abdbe960632e4b2309675288dbea9'
    city_name = input("Enter city name: ")
    
    get_weather(api_key, city_name)

