#For testing Parsers :P
from Parser import *

parsed_inicator = Parser.variable_sized_indicator('Gas Alarms\Variable-Sized_Indicator_Template.rpc')

parsed_readout = Parser.variable_sized_readout('Drives 4\Variable-Sized_Readout_Template.rpc')

parsed_control_button = Parser.variable_sized_control_button('Drives 4\Variable-Sized_Control_Button_Template.rpc')

parsed_static_graphic_data_line = Parser.static_graphic_data_line('Drives 4\Static_Graphic_Data_Line_Elements.rpc')

parsed_static_graphic_data_rectangle = Parser.static_graphic_data_rectangle('Drives 4\Static_Graphic_Data_Rectangle_Elements.rpc')

parsed_static_graphic_data_text = Parser.static_graphic_data_text('Drives 4\Static_Graphic_Data_Text_Elements.rpc')

parsed_grapic = Parser.variable_sized_graphic('Drives 4\Variable-Sized_Graphic_Template.rpc')
print(parsedVisualOrders)