import customtkinter as ctk
from .horizontal_scroll import hourly_weather_data
from .image_weather import WeatherImage

class HourlyData(ctk.CTkFrame):
    def __init__(self, child_master: object, count_image: int, **kwargs):
        self.COUNT_IMAGE = count
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width= 50,
            height= 200,
            border_width= 2,
            fg_color= '#5DA7B1',
            **kwargs
        )
        self.grid(row= 0, column= self.COUNT_IMAGE, padx = 20)
        #
        self.TIME = ctk.CTkLabel(
            master= self,
            text = "Time",
            font= ("Arial", 32, "bold")  
                      
        )
        self.TIME.pack(anchor = 'center', pady = 5)
        #
        self.IMAGE = WeatherImage(
            child_master= self, 
            size= (50, 50), 
            name_json= 'config_forecast.json',
            count = self.COUNT_IMAGE
        )
        self.IMAGE.pack(anchor = 'center', pady = 20)
        

for count in range(8):
    hourly_data_frame = HourlyData(child_master= hourly_weather_data, count_image= count)