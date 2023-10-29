# Parser for Variable-Sized_Indicator_Template data 
# *Warning, this class may contain too much VooDoo*

from Sub_Parsers import *

class Variable_Sized_Indicator:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(visual_order_elements):

        #Visual Order String Variables
        elements = ['Visual Order:','X Origin:','Y Origin:',
                    'X Size:','Y Size:',
                    'Refresh Affected Graphics Online?',
                    'Enable Conditional Visibility?',
                    'Visibility Expression:','Alarm Device Name:']
        # Visual Order Indicator States table String Variables
        key_alarm_message = 'Alarm Message'
        key_pen_color = 'Pen Color'
        key_fill_color = 'Fill Color'
        key_alarm = 'Alarm'
        key_alarmAck = 'Alarm Ack'
        key_conditional_expression = 'Conditional Expression'

        visual_orders = {}
        for visual_order_element in visual_order_elements:
            visual_order = {}
            elements_working = elements[:]
            for line in visual_order_element: #Parse each Visual Order values

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
                        val_alarm = 'Yes'
                        val_alarmAck = 'Yes'
                        pos_alarm = line.find(' Yes Yes ')
                        pos_conditional_expression = pos_alarm + len((' Yes Yes '))
                    elif (line.find(' No Yes ') != -1):
                        val_alarm = 'No'
                        val_alarmAck = 'Yes'
                        pos_alarm = line.find(' No Yes ')
                        pos_conditional_expression = pos_alarm + len((' No Yes '))
                    elif (line.find(' Yes No ') != -1):
                        val_alarm = 'Yes'
                        val_alarmAck = 'No'
                        pos_alarm = line.find(' Yes No ')
                        pos_conditional_expression = pos_alarm + len((' Yes No '))
                    elif (line.find(' No No ') != -1):
                        val_alarm = 'No'
                        val_alarmAck = 'No'
                        pos_alarm = line.find(' No No ')
                        pos_conditional_expression = pos_alarm + len((' No No '))

                    #derive expresion for Conditional Expression value
                    if 'pos_conditional_expression' in locals():
                        val_conditional_expression = line[pos_conditional_expression:].strip('\n')
                        line = line[:pos_alarm] #remove extracted values from current line

                    #derive Fill Color Visual Order value and strip it off
                    if line[len(line) - 1].isnumeric():
                        val_fill_color = line[line.rfind(' ') + 1 :]
                        line = line[:line.rfind(' ')]

                    #derive Pen Color and Alarm Message values from remaining portion of line 
                    if line[len(line) - 1].isnumeric():
                        val_pen_color = line[line.rfind(' ') + 1:]
                        val_alarm_message = line[:line.rfind(' ')]

                    #add all derived Indicator States to visualOrder
                    if ('val_alarm_message' in locals() and 
                        'val_pen_color' in locals() and 
                        'val_fill_color' in locals() and 
                        'val_alarm' in locals() and 
                        'val_alarmAck' in locals() and 
                        'val_conditional_expression' in locals()):
                        visual_order.update({'Indicator States' :
                                            {key_alarm_message : val_alarm_message,
                                            key_pen_color : val_pen_color,
                                            key_fill_color : val_fill_color,
                                            key_alarm : val_alarm,
                                            key_alarmAck : val_alarmAck,
                                            key_conditional_expression : val_conditional_expression}})

                #This voodoo should parse out anything in the elements list
                if elements_working:
                    for member in enumerate(elements_working[:]):  #enumerate copied ([:]) elements to loop through them in order they're stored
                        if (member[1] in line):
                            if len(elements_working) > 1:
                                parsed_element = Sub_Parsers.element_parser(member[1], elements_working[elements_working.index(member[1]) + 1], line)
                            else: 
                                #no next member
                                parsed_element = Sub_Parsers.element_parser(member[1], line[:len(line)], line)
                            visual_order.update(parsed_element.get('element')) 
                            line = parsed_element.get('remaining_line')
                            elements_working.remove(member[1])
                            if not line.strip():
                                break

            #Create dictionary of all VS_Indicator Visual Order elements         
            visual_orders.update({visual_order['Visual Order'] : visual_order}) #wow, thats a confusing line!

        return visual_orders