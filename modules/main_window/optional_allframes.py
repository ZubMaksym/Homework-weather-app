from .main_frame import mainframe, HEIGHT
import customtkinter

scrollabel_frame = customtkinter.CTkScrollableFrame(
    master= mainframe,
    width= 275,
    height= HEIGHT,
    fg_color= '#096C82',
)

scrollabel_frame.grid(row= 0, column= 0)