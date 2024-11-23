import customtkinter as ctk
from ..wr_json import scan_json
from .main_frame import mainframe
from ..request_api import request_time_zone

class TimeFrame(ctk.CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master= child_master,
            fg_color= '#4599A4',
            width= 360,
            height= 260,
            **kwargs
        )
        data_time = scan_json("timezine_forecast.json")
        self.place(x= 720, y= 80)
        request_time_zone()

        self.CURRENT_TIME_TITLE = ctk.CTkLabel(
            master= self,
            text= "Current Time",
            font= ('Roboto Slab', 24, 'bold'),
            text_color= '#FFFFFF'
        )

        self.CURRENT_TIME = ctk.CTkLabel(
            master= self,
            text= data_time["datetime"][11:16],
            font= ('Roboto Slab', 68, 'bold'),
            text_color= '#FFFFFF'
        )

        self.CURRENT_DATE = ctk.CTkLabel(
            master= self,
            text= data_time["datetime"][0:10],
            font= ('Roboto Slab', 24, 'bold'),
            text_color= '#FFFFFF'
        )

        self.DAY_OF_THE_WEEK = ctk.CTkLabel(
            master= self,
            text= data_time["day_of_week"],
            font= ('Roboto Slab', 24, 'bold'),
            text_color= '#FFFFFF'
        )

        self.CURRENT_TIME_TITLE.place(x= 103, y= 80)
        self.CURRENT_TIME.place(x= 90, y=105)
        self.CURRENT_DATE.place(x= 117, y=220)
        self.DAY_OF_THE_WEEK.place(x= 130, y=15)

frame_time = TimeFrame(child_master= mainframe)