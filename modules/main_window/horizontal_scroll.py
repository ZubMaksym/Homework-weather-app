import customtkinter as ctk
from .main_frame import mainframe


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

hourly_weather_data = HourlyWeatherData(child_master= mainframe)