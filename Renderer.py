# Class to hold all the different renderers

from Variable_Sized_Indicator_Renderer import *
from Variable_Sized_Readout_Renderer import *
from Variable_Sized_Control_Button_Renderer import *
from Variable_Sized_Graphic_Renderer import *
from Static_Graphic_Data_Line_Elements_Renderer import *
from Static_Graphic_Data_Rectangle_Elements_Renderer import *
from Static_Graphic_Data_Text_Elements_Renderer import *

class Render:
    
    def static_grapic_data_line(parsed_data):
        return render_visual_order(parsed_data)
         
    

    def static_graphic_data_rectangle(parsed_data):
        return parsed_data
    

    def static_graphic_data_text(parsed_data):
        return parsed_data
    

    def variable_sized_indicator(parsed_data):
        return parsed_data
    

    def variable_sized_readout(parsed_data):
        return parsed_data
    

    def variable_sized_control_button(parsed_data):
        return parsed_data
    

    def variable_sized_graphic(parsed_data):
        return parsed_data