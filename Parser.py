#Class to hold all the different parsers

from VSIndicatorParser import *

class Parser:
    def vSIndicator(preprocessedVS_IndicatorFilename):
        # Read in lines of preprocessed file
        preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
        preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

        # remove page breaks
        preprocessedVS_IndicatorFileLines = VSIndicator.removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

        # seperate Visual Orders
        visualOrderElementsList = VSIndicator.seperateVSIndicatorVisualOrders(preprocessedVS_IndicatorFileLines)

        # parse seperated Visual Orders
        parsedVSIndicatorVisualOrders = VSIndicator.parseVisualOrders(visualOrderElementsList)

        return parsedVSIndicatorVisualOrders