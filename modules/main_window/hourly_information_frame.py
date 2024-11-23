import customtkinter as ctk
from .horizontal_scroll import hourly_weather_data
from .image_weather import WeatherImage
from ..wr_json import scan_json

data_weather = scan_json(name_file= 'config_forecast.json')

class HourlyData(ctk.CTkFrame):
    def __init__(self, child_master: object, count: int= 0, **kwargs):
        self.COUNT = count
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color= '#5DA7B1',
            **kwargs
        )
        self.grid(row= 0, column= self.COUNT, padx = 20)
        #
        if self.COUNT == 0:
            self.TIME = ctk.CTkLabel(
                master= self,
                text = 'Now',
                font= ("Arial", 32, "bold")          
            )
        else:
            self.TIME = ctk.CTkLabel(
                master= self,
                text = data_weather['list'][self.COUNT]['dt_txt'][11:16],
                font= ("Arial", 32, "bold")  
            )
        self.TIME.pack(anchor = 'center', pady = 5)
        #
        self.IMAGE = WeatherImage(
            child_master= self, 
            size= (80, 80), 
            name_json= 'config_forecast.json',
            count = self.COUNT
        )
        self.IMAGE.pack(anchor = 'center', pady = 20)
        #
        self.TEMP = ctk.CTkLabel(
            master= self,
            text= f"{int(data_weather['list'][self.COUNT]['main']['temp'])}°",
            font= ("Arial", 32, "bold") 
        )
        self.TEMP.pack(anchor = 'center')

        
        

for count in range(8):
    hourly_data_frame = HourlyData(child_master= hourly_weather_data, count= count)