import customtkinter
from ..wr_json import scan_json
import json

mainframe = customtkinter.CTk(fg_color="#5DA7B1")
#
main_config = scan_json(name_file= "config.json")
# print(json.dumps(main_config, indent= 4))
#
WIDTH = main_config["main_frame"]["width"]
HEIGHT = main_config["main_frame"]["height"]
# 
mainframe.geometry(f"{WIDTH}x{HEIGHT}")