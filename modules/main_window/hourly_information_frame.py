import customtkinter as ctk
from .horizontal_scroll import hourly_weather_data


class HourlyData(ctk.CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width= 50,
            height= 200,
            border_width= 2,
            fg_color= '#5DA7B1',
            **kwargs
        )
        self.pack(anchor = "w")
        self.TIME = ctk.CTkLabel(
            master= self,
            text = "Time",
            # fg_color= '#5DA7B1',
            font= ("Arial", 32, "bold")            
        )
        self.TIME.pack(anchor = 'center', pady = 5)
        

hourly_data_frame = HourlyData(child_master= hourly_weather_data)