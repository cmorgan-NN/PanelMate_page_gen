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

from Element_Parsers import *
class VSIndicator:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parseVisualOrders(visualOrderElementsList):

        #############
        # Variables #
        #############

        #Visual Order String Variables
        elements = ['Visual Order: ','X Origin: ','Y Origin: ',
                    'X Size: ','Y Size: ',
                    'Refresh Affected Graphics Online? ',
                    'Enable Conditional Visibility? ',
                    'Visibility Expression: ','Alarm Device Name: ']
        # Visual Order Indicator States table String Variables
        keyAlarmMessage = 'Alarm Message'
        keyPenColor = 'Pen Color'
        keyFillColor = 'Fill Color'
        keyAlarm = 'Alarm'
        keyAlarmAck = 'Alarm Ack'
        keyConditionalExpression = 'Conditional Expression'

        element_number = 0
        visualOrders = {}
        for unparsedVisualOrder in visualOrderElementsList:
            visualOrder = {}
            for line in unparsedVisualOrder: #Parse each Visual Order values
                
                ################
                # Parse line 1 #
                ################
                
                #This voodoo should parse out anything in the elements list
                #FIXME: Change this to work by member number
                for member in elements:
                    if (member in line):
                        parsed_element = Element_Parsers.element_parser(member, elements[elements.index(member) + 1], line)
                        visualOrder.update(parsed_element.get('element')) 
                        line = parsed_element.get('remaining_line')
                        elements.remove(member)

#                #extract Visual Order value
#                if (line.find(keyVisualOrder + ': ') == 0):  
#                    line = line.lstrip(keyVisualOrder + ': ')
#                    valVisualOrder = line[0:(line.find(' '))]  
#                    visualOrder.update({keyVisualOrder : valVisualOrder})
#                    line = line.lstrip(valVisualOrder + ' ')

#                #extract X Origin
#                if  (line.find(keyXOrigin + ': ') == 0):  
#                    line = line.lstrip(keyXOrigin + ': ') 
#                    valXOrigin = line[0:(line.find(' '))]  
#                    visualOrder.update({keyXOrigin : valXOrigin})
#                    line = line.lstrip(valXOrigin + ' ')
#
#                #extract Y Origin
#                if  (line.find(keyYOrigin + ': ') == 0):  
#                    line = line.lstrip(keyYOrigin + ': ') 
#                    valYOrigin = line[0:(line.find(' '))]  
#                    visualOrder.update({keyYOrigin : valYOrigin})
#                    line = line.lstrip(valYOrigin + ' ')
#
#                #extract X Size  
#                if  (line.find(keyXSize + ': ') == 0):  
#                    line = line.lstrip(keyXSize + ': ') 
#                    valXSize = line[0:(line.find(' '))]  
#                    visualOrder.update({keyXSize : valXSize})
#                    line = line.lstrip(valXSize + ' ')
#
#                #extract Y Size  
#                if  (line.find(keyYSize + ': ') == 0):  
#                    line = line.lstrip(keyYSize + ': ') 
#                    valYSize = line[0:(line.find(' '))]  
#                    visualOrder.update({keyYSize : valYSize})
#                    line = line.lstrip(valYSize + ' ')
#
#                ################
#                # Parse line 2 #
#                ################
#
#                #extract Refresh Affected Graphics Online
#                if  (line.find(keyRefreshAffectedGraphicsOnline + '? ') == 0):  
#                    line = line.lstrip(keyRefreshAffectedGraphicsOnline + '? ') 
#                    valRefreshAffectedGraphicsOnline = line[0:(line.find(' '))]  
#                    visualOrder.update({keyRefreshAffectedGraphicsOnline : valRefreshAffectedGraphicsOnline})
#
#                ################
#                # Parse line 3 #
#                ################
#
#                #extract Enable Conditional Visibility
#                if  (line.find(keyEnableConditionalVisibility + '? ') == 0):  
#                    line = line.lstrip(keyEnableConditionalVisibility + '? ') 
#                    valEnableConditionalVisibility = line[0:(line.find(' '))]  
#                    visualOrder.update({keyEnableConditionalVisibility : valEnableConditionalVisibility})
#                    line = line.lstrip(valEnableConditionalVisibility + ' ')
#
#                #extract Visibility Expression
#                if  (line.find(keyVisibilityExpression + ':') == 0):  
#                    line = line.lstrip(keyVisibilityExpression + ': ') 
#                    valVisibilityExpression = line[0:(line.find(' '))]  
#                    visualOrder.update({keyVisibilityExpression : valVisibilityExpression})
#
#                ################
#                # Parse line 4 #
#                ################
#
#                #extract Alarm Device Name
#                if  (line.find(keyAlarmDeviceName + ':') == 0):  
#                    line = line.lstrip(keyAlarmDeviceName + ': ') 
#                    valAlarmDeviceName = line[0:(line.find(' '))]  
#                    visualOrder.update({keyAlarmDeviceName : valAlarmDeviceName})
#
#                ########################
#                # Lines 5 - 12 Skipped #
#                ########################
#
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