# Class to hold all the different parsers

from Variable_Sized_Indicator_Parser import *
from Variable_Sized_Readout_Parser import *
from Variable_Sized_Control_Button_Parser import *
from Static_Graphic_Data_Line_Elements_Parser import *
from Static_Graphic_Data_Rectangle_Elements_Parser import *

from Parser_Utility import *

# rpc file preprocessor
def rpc_preprocessor(rpc_path_filename, rpc_type): 
   
 
    # Read in lines of Variable_Sized_Indicator rpc
    rpc_file = open(rpc_path_filename, 'r')
    rpc_data_raw = rpc_file.readlines()
 
    # Check to make sure rpc passed in is a valid type
    #  a propper rpc's type is the first line of the file
    if rpc_data_raw[0].find(rpc_type) == -1:
        raise Exception('Input rpc first line doesn not contain "' + rpc_type +'"') 
 
    # remove first line (the rpc type is no longer needed)
    rpc_data_type_rem = rpc_data_raw[1:]
 
    # remove page breaks
    rpc_data_pb_rem = Parser_Utility.remove_page_breaks(rpc_data_type_rem)
    
    # if Variable Size rpc, seperate Visual Orders
    if rpc_type.find('Variable-Sized') != -1:
        rpc_element_list = Parser_Utility.seperate_visual_orders(rpc_data_pb_rem)
    else:
        rpc_element_list = rpc_data_pb_rem

    return rpc_element_list

class Parser:
    def variable_sized_indicator(rpc_path):

        # prep rpc for parsing 
        rpc_pre = rpc_preprocessor(rpc_path, 'Variable-Sized Indicator Template(s)')        
        
        # parse seperated rpc
        rpc_parsed = Variable_Sized_Indicator.parse_visual_orders(rpc_pre)

        return rpc_parsed


    def variable_sized_readout(rpc_path):

        # prep rpc for parsing 
        rpc_pre = rpc_preprocessor(rpc_path, 'Variable-Sized Readout Template(s)')        

        # parse seperated rpc
        rpc_parsed = Variable_Sized_Readout.parse_visual_orders(rpc_pre)

        return rpc_parsed       


    def variable_sized_control_button(rpc_path):

        # prep rpc for parsing 
        rpc_pre = rpc_preprocessor(rpc_path, 'Variable-Sized Control Button Template(s)')        

        # parse seperated rpc
        rpc_parsed = Variable_Sized_Control_Button.parse_visual_orders(rpc_pre)       

        return rpc_parsed


    def static_graphic_data_line(rpc_path):
        
        # prep rpc for parsing 
        rpc_pre = rpc_preprocessor(rpc_path, 'Line Element(s)')        

        # parse seperated rpc
        rpc_parsed = Static_Graphic_Data_Line.parse_visual_orders(rpc_pre)

        return rpc_parsed


    def static_graphic_data_rectangle(rpc_path):
        
        # prep rpc for parsing 
        rpc_pre = rpc_preprocessor(rpc_path, 'Rectangle Element(s)')        

        # parse seperated rpc
        rpc_parsed = Static_Graphic_Data_Rectangle.parse_visual_orders(rpc_pre)

        return rpc_parsed  