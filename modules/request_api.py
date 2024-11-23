import requests
#
from .wr_json import scan_json
#
from .wr_json import create_json
#
import json
#
data_api = scan_json(name_file= 'config_api.json')
#
data_time_api = scan_json(name_file= 'timezone_config.json')
def request_api_data(city_index: int):
    API_KEY = data_api['api_key']
    #
    CITY_NAME = data_api['city_name'][city_index]
    #
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=ua"
    #
    response = requests.get(URL)
    #
    if response.status_code == 200:
        #
        data_dict = json.loads(response.content)
        #
        create_json(name_file= "config_weather.json", value_file= data_dict)
        #
        print(json.dumps(data_dict, indent= 4))
    else:
        #
        print(f"Error: {response.status_code}")


def request_time_zone():
    API_KEY = data_time_api["api_key"]
    LAT = data_time_api['lat']
    LON = data_time_api['lon']

    api_url = f"https://api.api-ninjas.com/v1/worldtime?lat={LAT}&lon={LON}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == 200:
        data_dict = json.loads(response.content)
        print(response.text)
        create_json(name_file= "timezine_forecast.json", value_file= data_dict)
        print(json.dumps(data_dict, indent= 4))
    else:
        print(f"Error: {response.status_code}")