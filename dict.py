weather_in_city = {"city": "Москва", "temperature": "20"}
weather_in_city["temperature"] = int(weather_in_city["temperature"]) - 5

print(weather_in_city.get("country", "Россия"))

print(weather_in_city)

weather_in_city["date"] = "27.05.2019"

print(len(weather_in_city))