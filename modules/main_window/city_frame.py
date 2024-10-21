import customtkinter
from .optional_allframes import scrollabel_frame
from ..wr_json import scan_json

# 
class CityFrame(customtkinter.CTkFrame):
    def __init__(self, master: object, **kwargs):
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
        self.DATA_WEATHER = scan_json(name_file= 'config_weather.json')
        #
        self.CURRENT_POSITION = customtkinter.CTkLabel(
            master= self,
            text= "Current Position",
            font= ('Roboto Slab', 16, 'bold'),
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
        self.CURRENT_POSITION.place(x= 14, y= 6)
        self.TEMP.place(x= 165, y= 6)
        #

for element in range(10):
    city_frame = CityFrame(master= scrollabel_frame)
