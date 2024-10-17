import customtkinter
from .optional_allframes import scrollabel_frame

citys_data = customtkinter.CTkFrame(
    master = scrollabel_frame,
    fg_color= '#4599A4',
    corner_radius= 20,
    border_width= 2,
    border_color= '#FFFFFF',
    width= 245,
    height= 105
    
)
citys_data.pack(anchor = 'center')
