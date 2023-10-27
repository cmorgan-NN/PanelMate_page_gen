#Class to hold all the different parsers

from VSIndicatorParser import *
from ParserUtility import *
class Parser:
    def vSIndicator(preprocessedVS_IndicatorFilename):
        # Read in lines of VS_Indicator rpc
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # Check to make sure rpc passed in is a Variable-Sized Indicator Template(s)
        if preprocessedVS_IndicatorFileLines_Raw[0].find('Variable-Sized Indicator Template(s)') == -1:
            raise Exception('Input rpc first line doesn not contain "Variable-Sized Indicator Template(s)"') 
        
        # remove first line (title of the rpc is not needed)
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFileLines_Raw[1:]
        # remove page breaks
        preprocessedVS_IndicatorFileLines = ParserUtility.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # seperate Visual Orders
        visualOrderElementsList = ParserUtility.seperateVisualOrders(preprocessedVS_IndicatorFileLines)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = VSIndicator.parseVisualOrders(visualOrderElementsList)

        return parsedVSIndicatorVisualOrders