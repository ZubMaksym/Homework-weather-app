import customtkinter as ctk
from .main_frame import mainframe
import os
from ..wr_json import scan_json
import PIL.Image as pil


class WeatherImage(ctk.CTkLabel):
    def __init__(
        self, 
        child_master: object, 
        name_json: str | None = None, 
        **kwargs
    ):
        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            image= self.load_image(),
            text= '',
            **kwargs
        )
        
    def load_image(self):
        #
        data_weather = scan_json(name_file= "config_weather.json")
        #
        image_name = data_weather['weather'][0]['icon']
        #
        image_path = os.path.abspath(__file__ + f"/../../../media/images/{image_name}.png")
        
        return ctk.CTkImage(
            light_image= pil.open(image_path), 
            size= (170, 160)
        )


image = WeatherImage(child_master= mainframe)
image.place(x= 380, y = 170)