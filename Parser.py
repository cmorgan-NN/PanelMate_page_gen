#Class to hold all the different parsers

from VS_Indicator_Parser import *
from VS_Readout_Parser import *
from VS_Control_Button_Parser import *
from Static_Graphic_Data_Line_Elements_Parser import *

from Parser_Utility import *

#FIXME: everything using "preprocessedVS_IndicatorFilename" 
class Parser:
    def variable_sized_indicator(preprocessedVS_IndicatorFilename):
        # Read in lines of VS_Indicator rpc
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # Check to make sure rpc passed in is a Variable-Sized Indicator Template(s)
        if preprocessedVS_IndicatorFileLines_Raw[0].find('Variable-Sized Indicator Template(s)') == -1:
            raise Exception('Input rpc first line doesn not contain "Variable-Sized Indicator Template(s)"') 
        
        # remove first line (title of the rpc is not needed)
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFileLines_Raw[1:]
        # remove page breaks
        preprocessedVS_IndicatorFileLines = Parser_Utility.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # seperate Visual Orders
        visualOrderElementsList = Parser_Utility.seperateVisualOrders(preprocessedVS_IndicatorFileLines)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = VS_Indicator.parseVisualOrders(visualOrderElementsList)

        return parsedVSIndicatorVisualOrders
    
    def variable_sized_readout(preprocessedVS_IndicatorFilename):
        # Read in lines of VS_Indicator rpc
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # Check to make sure rpc passed in is a Variable-Sized Indicator Template(s)
        if preprocessedVS_IndicatorFileLines_Raw[0].find('Variable-Sized Readout Template(s)') == -1:
            raise Exception('Input rpc first line doesn not contain "Variable-Sized Readout Template(s)"') 
        
        # remove first line (title of the rpc is not needed)
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFileLines_Raw[1:]
        # remove page breaks
        preprocessedVS_IndicatorFileLines = Parser_Utility.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # seperate Visual Orders
        visualOrderElementsList = Parser_Utility.seperateVisualOrders(preprocessedVS_IndicatorFileLines)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = VS_Readout.parseVisualOrders(visualOrderElementsList)

        return parsedVSIndicatorVisualOrders
    

    def variable_sized_control_button(preprocessedVS_IndicatorFilename):
        # Read in lines of VS_Indicator rpc
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # Check to make sure rpc passed in is a Variable-Sized Indicator Template(s)
        if preprocessedVS_IndicatorFileLines_Raw[0].find('Variable-Sized Control Button Template(s)') == -1:
            raise Exception('Input rpc first line doesn not contain "Variable-Sized Control Button Template(s)"') 
        
        # remove first line (title of the rpc is not needed)
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFileLines_Raw[1:]
        # remove page breaks
        preprocessedVS_IndicatorFileLines = Parser_Utility.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # seperate Visual Orders
        visualOrderElementsList = Parser_Utility.seperateVisualOrders(preprocessedVS_IndicatorFileLines)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = VS_Control_Button.parseVisualOrders(visualOrderElementsList)

        return parsedVSIndicatorVisualOrders


    def static_graphic_line_data(preprocessedVS_IndicatorFilename):
        # Read in lines of VS_Indicator rpc
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # Check to make sure rpc passed in is a Variable-Sized Indicator Template(s)
        if preprocessedVS_IndicatorFileLines_Raw[0].find('Line Element(s)') == -1:
            raise Exception('Input rpc first line doesn not contain "Line Element(s)"') 
        
        # remove first line (title of the rpc is not needed)
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFileLines_Raw[1:]

        # remove page breaks
        visual_order_elements_list = Parser_Utility.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = Static_Graphic_Data_Line.parseVisualOrders(visual_order_elements_list)

        return parsedVSIndicatorVisualOrders   