import customtkinter as ctk
from .main_frame import mainframe
import os
from ..wr_json import scan_json
import PIL.Image as pil


class WeatherImage(ctk.CTkLabel):
    def __init__(self, child_master: object, size: tuple, name_json: str, count: int = 0, **kwargs):

        self.NAME_JSON = name_json
        self.SIZE = size
        self.COUNT = count

        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            image= self.load_image(),
            text= '',
            **kwargs
        )
        
    def load_image(self):
        #
        data_weather = scan_json(name_file= self.NAME_JSON)
        #
        if 'weather' in self.NAME_JSON:
            image_name = data_weather['weather'][0]['icon']
        elif 'forecast' in self.NAME_JSON:
            image_name = data_weather['list'][self.COUNT]['weather'][0]['icon']
        #
        image_path = os.path.abspath(__file__ + f"/../../../media/images/{image_name}.png")
        
        return ctk.CTkImage(
            light_image= pil.open(image_path), 
            size= self.SIZE
        )


image = WeatherImage(child_master= mainframe, name_json= "config_weather.json", size= (170, 160))
image.place(x= 380, y = 170)