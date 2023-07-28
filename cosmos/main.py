import requests
import time


# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
base_url = "http://api.open-notify.org/iss-now.json"

while True:
    response = requests.get(url=base_url)
    data = response.json()
    result = f'{data["iss_position"]["longitude"]};{data["iss_position"]["latitude"]}\n'
    print(result, end='')

    with open('stats/coordinates.csv', 'a') as file:
        file.write(result)
    time.sleep(5)