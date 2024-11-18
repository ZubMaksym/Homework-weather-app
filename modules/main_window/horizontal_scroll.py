import customtkinter as ctk
from .main_frame import mainframe
from ..wr_json import scan_json, create_json
import requests

class HourlyWeatherData(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self,
            master = child_master,
            border_width = 5,
            corner_radius = 20,
            border_color = '#FFFFFF',
            width = 820,
            height = 240,
            scrollbar_fg_color = '#00FFFF',
            orientation= 'horizontal',
            fg_color= '#5DA7B1',
            **kwargs
        )

        self.place(x = 325, y = 430)
        self.request_api_forecast()

    def request_api_forecast(self):
        CONFIG_WEATHER = scan_json(name_file= 'config_api.json')
        CITY_NAME = CONFIG_WEATHER["city_name"][0]
        API_KEY = CONFIG_WEATHER['api_key']
        URL = CONFIG_WEATHER['forecast_weather'].format(CITY_NAME, API_KEY)# ''.format()
        try:
            response = requests.get(URL)
            data_forecast = response.json()
            create_json(name_file= 'config_forecast.json', value_file= data_forecast)

        except requests.exceptions.RequestException as exception:
            print(f"Error getting: {exception}")
        

hourly_weather_data = HourlyWeatherData(child_master= mainframe)