#For testing Parsers :P
from Parser import *

parsed_inicators = Parser.variable_sized_indicator('Gas Alarms\Variable-Sized_Indicator_Template.rpc')

parsed_readout = Parser.variable_sized_readout('Drives 4\Variable-Sized_Readout_Template.rpc')

parsed_control_button = Parser.variable_sized_control_button('Drives 4\Variable-Sized_Control_Button_Template.rpc')

print(parsedVisualOrders)