import customtkinter
from .optional_allframes import scrollabel_frame
from ..wr_json import scan_json
from ..request_api import request_api_data, data_api
#
cities_names = ['Dnipro', 'Kyiv', 'Lviv', 'Rome', 'London']
# 
class CityFrame(customtkinter.CTkFrame):
    def __init__(self, master: object, city_index: int, **kwargs):
        customtkinter.CTkFrame.__init__(
            self, 
            master= master, 
            fg_color= '#4599A4',
            corner_radius= 20,
            border_width= 2,
            border_color= '#FFFFFF',
            width= 245,
            height= 105,
            **kwargs
        )
        self.pack(anchor = 'center', pady= 10)
        self.CITY_INDEX = city_index
        #
        self.request_api()
        #
        self.DATA_WEATHER = scan_json(name_file= 'config_weather.json')
        #
        if city_index == 0:
            self.CURRENT_POSITION = customtkinter.CTkLabel(
                master= self,
                text= "Current Position",
                font= ('Roboto Slab', 16, 'bold'),
                text_color= '#FFFFFF'
            )
            self.CITY_TIME = customtkinter.CTkLabel(
                master= self,
                text= self.DATA_WEATHER['name'],
                font= ('Roboto Slab', 12, 'bold'),
                text_color= '#FFFFFF'
            )
        else:
            self.CURRENT_POSITION = customtkinter.CTkLabel(
                master= self,
                text= self.DATA_WEATHER['name'],
                font= ('Roboto Slab', 16, 'bold'),
                text_color= '#FFFFFF'
            )
            self.CITY_TIME = customtkinter.CTkLabel(
                master= self,
                text= '20:40',
                font= ('Roboto Slab', 12, 'bold'),
                text_color= '#FFFFFF'
            )
        #
        self.TEMP = customtkinter.CTkLabel(
            master= self,
            text= f"{int(self.DATA_WEATHER['main']['temp'])}°",
            font= ('Roboto Slab', 50, 'bold'),
            text_color= '#FFFFFF'
        )
        #
        self.DESCRIPTION_WEATHER = customtkinter.CTkLabel(
            master = self,
            text = self.DATA_WEATHER["weather"][0]["description"],
            font = ('Roboto Slab', 12, 'bold'),
            text_color = '#FFFFFF'
        )
        #
        self.CURRENT_POSITION.place(x= 14, y= 6)
        self.TEMP.place(x= 165, y= 6)
        self.DESCRIPTION_WEATHER.place(x = 14, y = 60)
        self.CITY_TIME.place(x= 14, y= 30)
        #
    def request_api(self):
        request_api_data(city_index= self.CITY_INDEX)
        
for element in range(len(data_api['city_name'])):
    city_frame = CityFrame(master= scrollabel_frame, city_index= element)
