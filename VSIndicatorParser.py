# Parser for Variable-Sized_Indicator_Template data 
# *Warning, this class may contain too much VooDoo*

# NOTE Background Info
# every VO is 13 lines long after removing page breaks
# example:
# Visual Order: 5 X Origin: 0 Y Origin: 278 X Size: 56 Y Size: 16
# Refresh Affected Graphics Online? No
# Enable Conditional Visibility? No Visibility Expression:
# Alarm Device Name:
# Indicator States 
# Alarm Message Pen
# Color
# Fill
# Color
# Alarm Alarm
# Ack
# Conditional Expression
# Zone 5 Fan #1 PSI Sw. Out 3 0 Yes Yes [%M0945]
#
# Everything below Indicator States is a dict nested in Indicator States
#   this dict is a representation of a table from the PanelMate report
class VSIndicator:
    ############# 
    # Functions #
    #############

    # Function to remove page breaks from PanelMate 
    #   preprocessed Variable-Sized_Indicator_Template report elements 
    def removePageBreaks(preprocessedVS_IndicatorFileLines_Raw):
        #find page breaks
        lineNumber = 0
        pageBreakLines = []
        for line in preprocessedVS_IndicatorFileLines_Raw:
            lineNumber += 1
            if 'Page' and 'Configuration' in line: #the page line contains Page and Configuration
                pageBreakLines.append(lineNumber - 1) #the line before a page line is unwanted
                pageBreakLines.append(lineNumber)
                pageBreakLines.append(lineNumber + 1) #and the line after a page line is unwanted

        #create a new list of data without page breaks
        lineNumber = 0
        preprocessedVS_IndicatorFileLines = []
        for line in preprocessedVS_IndicatorFileLines_Raw:
            lineNumber += 1
            if lineNumber not in pageBreakLines:
                preprocessedVS_IndicatorFileLines.append(line)

        #passback data
        return preprocessedVS_IndicatorFileLines


    # Function to seperate visual orders and return list
    def seperateVSIndicatorVisualOrders(preprocessedVS_IndicatorFileLines):
        VSIndicatorVOs = []
        VSIndicatorVO= []
        lineNumber = 0

        for line in preprocessedVS_IndicatorFileLines:# A Visual Order is always 13 lines long
            lineNumber += 1
            VSIndicatorVO.append(line) 
            if (lineNumber == 13):     
                lineNumber = 0
                VSIndicatorVOs.append(VSIndicatorVO.copy())
                VSIndicatorVO.clear()

        return VSIndicatorVOs


    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parseVisualOrders(visualOrderElementsList):

        #############
        # Variables #
        #############

        #Visual Order String Variables
        keyVisualOrder = 'Visual Order'
        keyXOrigin = 'X Origin'
        keyYOrigin = 'Y Origin'
        keyXSize = 'X Size'
        keyYSize = 'Y Size'
        keyRefreshAffectedGraphicsOnline = 'Refresh Affected Graphics Online'
        keyEnableConditionalVisibility = 'Enable Conditional Visibility'
        keyVisibilityExpression = 'Visibility Expression'
        keyAlarmDeviceName = 'Alarm Device Name'
        # Visual Order Indicator States table String Variables
        keyAlarmMessage = 'Alarm Message'
        keyPenColor = 'Pen Color'
        keyFillColor = 'Fill Color'
        keyAlarm = 'Alarm'
        keyAlarmAck = 'Alarm Ack'
        keyConditionalExpression = 'Conditional Expression'

        visualOrders = {}
        for unparsedVisualOrder in visualOrderElementsList:
            visualOrder = {}
            for line in unparsedVisualOrder: #Parse each Visual Order values

                ################
                # Parse line 1 #
                ################

                #extract Visual Order value
                if (line.find(keyVisualOrder + ': ') == 0):  
                    line = line.lstrip(keyVisualOrder + ': ')
                    valVisualOrder = line[0:(line.find(' '))]  
                    visualOrder.update({keyVisualOrder : valVisualOrder})
                    line = line.lstrip(valVisualOrder + ' ')

                #extract X Origin
                if  (line.find(keyXOrigin + ': ') == 0):  
                    line = line.lstrip(keyXOrigin + ': ') 
                    valXOrigin = line[0:(line.find(' '))]  
                    visualOrder.update({keyXOrigin : valXOrigin})
                    line = line.lstrip(valXOrigin + ' ')

                #extract Y Origin
                if  (line.find(keyYOrigin + ': ') == 0):  
                    line = line.lstrip(keyYOrigin + ': ') 
                    valYOrigin = line[0:(line.find(' '))]  
                    visualOrder.update({keyYOrigin : valYOrigin})
                    line = line.lstrip(valYOrigin + ' ')

                #extract X Size  
                if  (line.find(keyXSize + ': ') == 0):  
                    line = line.lstrip(keyXSize + ': ') 
                    valXSize = line[0:(line.find(' '))]  
                    visualOrder.update({keyXSize : valXSize})
                    line = line.lstrip(valXSize + ' ')

                #extract Y Size  
                if  (line.find(keyYSize + ': ') == 0):  
                    line = line.lstrip(keyYSize + ': ') 
                    valYSize = line[0:(line.find(' '))]  
                    visualOrder.update({keyYSize : valYSize})
                    line = line.lstrip(valYSize + ' ')

                ################
                # Parse line 2 #
                ################

                #extract Refresh Affected Graphics Online
                if  (line.find(keyRefreshAffectedGraphicsOnline + '? ') == 0):  
                    line = line.lstrip(keyRefreshAffectedGraphicsOnline + '? ') 
                    valRefreshAffectedGraphicsOnline = line[0:(line.find(' '))]  
                    visualOrder.update({keyRefreshAffectedGraphicsOnline : valRefreshAffectedGraphicsOnline})

                ################
                # Parse line 3 #
                ################

                #extract Enable Conditional Visibility
                if  (line.find(keyEnableConditionalVisibility + '? ') == 0):  
                    line = line.lstrip(keyEnableConditionalVisibility + '? ') 
                    valEnableConditionalVisibility = line[0:(line.find(' '))]  
                    visualOrder.update({keyEnableConditionalVisibility : valEnableConditionalVisibility})
                    line = line.lstrip(valEnableConditionalVisibility + ' ')

                #extract Visibility Expression
                if  (line.find(keyVisibilityExpression + ':') == 0):  
                    line = line.lstrip(keyVisibilityExpression + ': ') 
                    valVisibilityExpression = line[0:(line.find(' '))]  
                    visualOrder.update({keyVisibilityExpression : valVisibilityExpression})

                ################
                # Parse line 4 #
                ################

                #extract Alarm Device Name
                if  (line.find(keyAlarmDeviceName + ':') == 0):  
                    line = line.lstrip(keyAlarmDeviceName + ': ') 
                    valAlarmDeviceName = line[0:(line.find(' '))]  
                    visualOrder.update({keyAlarmDeviceName : valAlarmDeviceName})

                ########################
                # Lines 5 - 12 Skipped #
                ########################

                ##################
                # Parse Line 13  #
                ##################

                # Create sub dictionary Indicator States

                #the remaining values are all on one line without keys seperating them
                # we will get our bearings by finding the pair of "Yes/No" possibilities 
                # which represent the Alarm and Alarm Ack values and parse the rest of the
                # line based on this location
                # Note that this solution does not account for this string being used as the
                # Conditional Expression value
                if (line.find(' Yes Yes ') != -1):
                    valAlarm = 'Yes'
                    valAlarmAck = 'Yes'
                    posAlarm = line.find(' Yes Yes ')
                    posConditionalExpression = posAlarm + len((' Yes Yes '))
                elif (line.find(' No Yes ') != -1):
                    valAlarm = 'No'
                    valAlarmAck = 'Yes'
                    posAlarm = line.find(' No Yes ')
                    posConditionalExpression = posAlarm + len((' No Yes '))
                elif (line.find(' Yes No ') != -1):
                    valAlarm = 'Yes'
                    valAlarmAck = 'No'
                    posAlarm = line.find(' Yes No ')
                    posConditionalExpression = posAlarm + len((' Yes No '))
                elif (line.find(' No No ') != -1):
                    valAlarm = 'No'
                    valAlarmAck = 'No'
                    posAlarm = line.find(' No No ')
                    posConditionalExpression = posAlarm + len((' No No '))

                #derive expresion for Conditional Expression value
                if 'posConditionalExpression' in locals():
                    valConditionalExpression = line[posConditionalExpression:].strip('\n')
                    line = line[:posAlarm] #remove extracted values from current line

                #derive Fill Color Visual Order value and strip it off
                if line[len(line) - 1].isnumeric():
                    valFillColor = line[line.rfind(' ') + 1 :]
                    line = line[:line.rfind(' ')]

                #derive Pen Color and Alarm Message values from remaining portion of line 
                if line[len(line) - 1].isnumeric():
                    valPenColor = line[line.rfind(' ') + 1:]
                    valAlarmMessage = line[:line.rfind(' ')]

                #add all derived Indicator States to visualOrder
                if ('valAlarmMessage' in locals() and 
                    'valPenColor' in locals() and 
                    'valFillColor' in locals() and 
                    'valAlarm' in locals() and 
                    'valAlarmAck' in locals() and 
                    'valConditionalExpression' in locals()):
                    visualOrder.update({'Indicator States' :
                                        {keyAlarmMessage : valAlarmMessage,
                                        keyPenColor : valPenColor,
                                        keyFillColor : valFillColor,
                                        keyAlarm : valAlarm,
                                        keyAlarmAck : valAlarmAck,
                                        keyConditionalExpression : valConditionalExpression}})

            #Create dictionary of all VS_Indicator Visual Order elements         
            visualOrders.update({visualOrder['Visual Order'] : visualOrder}) #wow, thats a confusing line!

        return visualOrders