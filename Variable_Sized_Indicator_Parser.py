# Parser for Variable-Sized_Indicator_Template data 
# *Warning, this class may contain too much VooDoo*

from Sub_Parsers import *

class Variable_Sized_Indicator:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(visualOrderElementsList):

        #Visual Order String Variables
        elements = ['Visual Order:','X Origin:','Y Origin:',
                    'X Size:','Y Size:',
                    'Refresh Affected Graphics Online?',
                    'Enable Conditional Visibility?',
                    'Visibility Expression:','Alarm Device Name:']
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
            elements_working = elements[:]
            for line in unparsedVisualOrder: #Parse each Visual Order values

                if line[len(line) - 1] != '\n':
                     line = line + '\n'

                # Create sub dictionary Indicator States

                #the remaining values are all on one line without keys seperating them
                # we will get our bearings by finding the pair of "Yes/No" possibilities 
                # which represent the Alarm and Alarm Ack values and parse the rest of the
                # line based on this location
                # Note that this solution does not account for this string being used as the
                # Conditional Expression value
                if not elements_working:
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

                #This voodoo should parse out anything in the elements list
                if elements_working:
                    for member in enumerate(elements_working[:]):  #enumerate copied ([:]) elements to loop through them in order they're stored
                        if (member[1] in line):
                            if len(elements_working) > 1:
                                parsed_element = Sub_Parsers.element_parser(member[1], elements_working[elements_working.index(member[1]) + 1], line)
                            else: 
                                #no next member
                                parsed_element = Sub_Parsers.element_parser(member[1], line[:len(line)], line)
                            visualOrder.update(parsed_element.get('element')) 
                            line = parsed_element.get('remaining_line')
                            elements_working.remove(member[1])
                            if not line.strip():
                                break

            #Create dictionary of all VS_Indicator Visual Order elements         
            visualOrders.update({visualOrder['Visual Order'] : visualOrder}) #wow, thats a confusing line!

        return visualOrders