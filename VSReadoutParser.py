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

from Sub_Parsers import *

class VSReadout:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parseVisualOrders(visualOrderElementsList):

        #Visual Order String Variables
        elements = ['Visual Order:','X Origin:','Y Origin:',
                    'X Size:','Y Size:','Font:','Deadband Range:',
                    'Alarm Ack:','Refresh Affected Graphics Online?',
                    'Enable Conditional Visibility?','Visibility Expression:',
                    'Foreground Color:','Background Color:','Text Direction:',
                    'Decimal Places:','Control Arrow Position:',
                    'Control Arrow Display Flag:','Alarm Device Name:',
                    'Value Expression:','High Alarm Expression:',
                    'Low Alarm Expression:']
        control_definitions = ['Input Value Expression:',
                               'Target Word Address:',
                               'Password Protection:']


        visualOrders = {}
        for unparsedVisualOrder in visualOrderElementsList:
            visualOrder = {}
            elements_working = elements[:]
            control_definitions_working = control_definitions[:]

            for line in unparsedVisualOrder: #Parse each Visual Order values
                
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

                #And this other voodoo should parse out a Control Definitions sub-dictionary
                if any('Control Definitions' in item for item in unparsedVisualOrder):   
                    if 'control_definitions_D' not in locals():
                        control_definitions_D = {}                    
                    if control_definitions_working:
                        for member in enumerate(control_definitions_working[:]):  #enumerate copied ([:]) elements to loop through them in order they're stored
                            if (member[1] in line):
                                if len(control_definitions_working) > 1:
                                    parsed_element = Sub_Parsers.element_parser(member[1], control_definitions_working[control_definitions_working.index(member[1]) + 1], line)
                                else: 
                                    #no next member
                                    parsed_element = Sub_Parsers.element_parser(member[1], line[:len(line)], line)
                                control_definitions_D.update(parsed_element.get('element')) 
                                line = parsed_element.get('remaining_line')
                                control_definitions_working.remove(member[1])
                                if not line.strip():
                                    break
                    if not control_definitions_working:            
                        visualOrder.update({'Control Definitions' : control_definitions_D.copy()})
                   
            #Create dictionary of all VS_Indicator Visual Order elements         
            visualOrders.update({visualOrder['Visual Order'] : visualOrder}) #wow, thats a confusing line!

        return visualOrders