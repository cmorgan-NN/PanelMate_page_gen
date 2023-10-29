# Parser for Variable-Sized_Control_Button_Template data 

from Sub_Parsers import *

class Variable_Sized_Control_Button:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(visualOrderElementsList):

        #Visual Order String Variables
        elements = ['Visual Order:','X Origin:','Y Origin:',
                    'X Size:','Y Size:',
                    'Refresh Affected Graphics Online?',
                    'Enable Conditional Visibility?','Visibility Expression:',
                    'Lens Color:','Control Type:']
        
        visualOrders = {}
        for unparsedVisualOrder in visualOrderElementsList:
            visualOrder = {}
            if 'elements_working' in locals():
                elements_working.clear()
            elements_working = elements[:]

            if any('Page Change' in item for item in unparsedVisualOrder):
                    elements_working.append('Expression:')
            if any('Normaly Open, Momentary' in item for item in unparsedVisualOrder):
                    elements_working.append('Reference:')

            for line in unparsedVisualOrder: #Parse each Visual Order values

                if line[len(line) - 1] != '\n':
                     line = line + '\n'

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