# Parser for Variable-Sized_Readout_Template data 

# NOTE Background Info
# example:
# Visual Order: 31 X Origin: 29 Y Origin: 243 X Size: 24 Y Size: 16 Font: Normal Deadband Range: 0% Alarm Ack: Yes
# Refresh Affected Graphics Online? No
# Enable Conditional Visibility? No Visibility Expression:
# Foreground Color: 6 Background Color: 0 Text Direction: Horizontal
# Decimal Places: 0
# Control Arrow Position: Left Control Arrow Display Flag: Always
# Alarm Device Name:
# Value Expression: [%R0012]
# High Alarm Expression:
# Low Alarm Expression:

class VSReadout:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parseVisualOrders(visualOrderElementsList):

        #############
        # Variables #
        #############

        #Visual Order String Variables

        #Line 1
        keyVisualOrder = 'Visual Order'
        keyXOrigin = 'X Origin'
        keyYOrigin = 'Y Origin'
        keyXSize = 'X Size'
        keyYSize = 'Y Size'
        keyFont = 'Font'
        keyDeadbandRange = 'Deadband Range'
        keyAlarmAck = 'Alarm Ack'

        #Line 2
        keyRefreshAffectedGraphicsOnline = 'Refresh Affected Graphics Online'

        #Line 3
        keyEnableConditionalVisibility = 'Enable Conditional Visibility'
        keyVisibilityExpression = 'Visibility Expression'
        
        #Line 4
        keyForegroundColor = 'Foreground Color'
        keyBackgroundColor = 'Background Color'
        keyTextDirection = 'Text Direction'

        #Line 5
        keyDecimalPlaces = 'Decimal Places'

        #Line 6
        keyControlArrowPosition = 'Control Arrow Position' 
        keyControlArrowDisplayFlag = 'Control Arrow Display Flag'

        #Line 7
        keyAlarmDeviceName = 'Alarm Device Name'

        #Line 8
        keyValueExpression = 'Value Expression'

        #Line 9
        keyHighAlarmExpression = 'High Alarm Expression'

        #Line 10
        keyLowAlarmExpression = 'Low Alarm Expression'


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

                #extract Font
                if  (line.find(keyFont + ': ') == 0):  
                    line = line.lstrip(keyFont + ': ') 
                    valFont = line[0:(line.find(' '))]  
                    visualOrder.update({keyFont : valFont})
                    line = line.lstrip(valFont + ' ')                   

                #extract Deadband Range
                if  (line.find(keyDeadbandRange + ': ') == 0):  
                    line = line.lstrip(keyDeadbandRange + ': ') 
                    valDeadbandRange = line[0:(line.find(' '))]  
                    visualOrder.update({keyDeadbandRange : valDeadbandRange})
                    line = line.lstrip(valDeadbandRange + ' ')                   

                #extract Alarm Ack
                if  (line.find(keyAlarmAck + ': ') == 0):  
                    line = line.lstrip(keyAlarmAck + ': ') 
                    valAlarmAck = line[0:(line.find(' '))]  
                    visualOrder.update({keyAlarmAck : valAlarmAck})
               
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

                #TODO: extract Foreground Color
                # keyForegroundColor = 'Foreground Color'
                if  (line.find(keyDeadbandRange + ': ') == 0):  
                    line = line.lstrip(keyDeadbandRange + ': ') 
                    valDeadbandRange = line[0:(line.find(' '))]  
                    visualOrder.update({keyDeadbandRange : valDeadbandRange})
                    line = line.lstrip(valDeadbandRange + ' ')                   

        
                #TODO: extract Background Color
                # keyBackgroundColor = 'Background Color'
                
                #TODO: extract Text Direction
                # keyTextDirection = 'Text Direction'

                ################
                # Parse line 5 #
                ################

                #TODO: extract Decimal Places
                # keyDecimalPlaces = 'Decimal Places'

                ################
                # Parse line 6 #
                ################
                
                #TODO: extract Control Arrow Position
                # keyControlArrowPosition = 'Control Arrow Position' 
 
                #TODO: extract Control Arrow Display Flag      
                # keyControlArrowDisplayFlag = 'Control Arrow Display Flag'

                ################
                # Parse line 7 #
                ################

                #extract Alarm Device Name
                if  (line.find(keyAlarmDeviceName + ':') == 0):  
                    line = line.lstrip(keyAlarmDeviceName + ': ') 
                    valAlarmDeviceName = line[0:(line.find(' '))]  
                    visualOrder.update({keyAlarmDeviceName : valAlarmDeviceName})

                ################
                # Parse line 8 #
                ################
 
                 #TODO: extract Value Expression      
                 # keyValueExpression = 'Value Expression'

                ################
                # Parse line 9 #
                ################
 
                #TODO: extract High Alarm Expression      
                # keyHighAlarmExpression = 'High Alarm Expression'

                #################
                # Parse line 10 #
                #################

                #TODO: extract Low Alarm Expression      
                # keyLowAlarmExpression = 'Low Alarm Expression'

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