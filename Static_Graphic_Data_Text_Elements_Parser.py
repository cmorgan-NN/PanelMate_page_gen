# Static Graphic Data Text Elements parser

from Sub_Parsers import *
from Parser_Utility import *

class Static_Graphic_Data_Text:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(visualOrderElementsList_raw):

        #Visual Order String Variables
        elements = ['Visual Order',
                    'X Origin',
                    'Y Origin',
                    'Refresh Affected Graphics Online',
                    'Enable Cond. Visibility',
                    'Visibility Expression',
                    'Font', 
                    'Foreground Color',
                    'Background Color',
                    'Text'] 
        
        visualOrderElementsList = Parser_Utility.remove_table_headings(elements, visualOrderElementsList_raw)        

        visualOrders = {}
        for line in visualOrderElementsList:
            visualOrder = {}

            #for EOF that are missing the newline
            if line[len(line) - 1] != '\n':
                 line = line + '\n'

            enable_cond_visibility = 'No' #FIXME: Ist this needed? Ein Bein Mein Komphf
            current_line_pos = 0 
            index_modifier = 0
            #This voodoo should parse out anything in an element table
            for index, member in enumerate(elements):  
                
                index = index - index_modifier #to manipulate index for blank values

                if (member == 'Visibility Expression' and 
                    visualOrder['Enable Cond. Visibility'] == 'No'):
                    index_modifier += 1 
                    parsed_element = { member : ''}
                elif (member == 'Visibility Expression' and
                    #NOTE: sometimes visibility expressions have more than just a reference in them,
                    # so they need to be run twice. This may need a better fix in the future
                    #NOTE: copilot mostly wrote the 4 lines below and the Double High font code below that. Neat...
                    # we only want to pass along the '] =?' part of the expression until render
                    # where it is rendered out as logic and changed from 0's and 1's to 
                    # True and False, respectively
                      '] =' in line):
                    next_parsed_element = Sub_Parsers.table_parser(member, index + 1, line)
                    parsed_element = Sub_Parsers.table_parser(member, index, line)
                    parsed_element = { member : parsed_element.get(member) + ' ' + next_parsed_element.get(member)}
                    index_modifier -= 1 #to manipulate index for extra word
                elif member != 'Text':    
                    parsed_element = Sub_Parsers.table_parser(member, index, line)
                    if member == 'Font' and parsed_element.get(member) == 'Double':
                        #since parsing trips on the space, double high font needs to be handled separately
                        next_parsed_element = Sub_Parsers.table_parser(member, index + 1, line)
                        parsed_element = { member : parsed_element.get(member) + ' ' + next_parsed_element.get(member)}
                        index_modifier -= 1 #to manipulate index for extra word
                elif member == 'Text':
                    parsed_element = { member : line[current_line_pos - 1:].strip() }
                visualOrder.update(parsed_element)

                #Accumulate number of chars before the Text element
                current_line_pos = current_line_pos + len(parsed_element.get(member)) + len(' ')  

            #Create dictionary of all VS_Indicator Visual Order elements         
            visualOrders.update({visualOrder['Visual Order'] : visualOrder}) #wow, thats a confusing line!

        return visualOrders