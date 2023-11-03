#TODO: Create the Variable Sized Graphic Template parser
#NOTE: VS Grapic Templates are funky, I think the X Y coordinates are not saved with them.
#       who knows if I'll ever be able to render them. Best to still make the parser tho.
# Can we work some more magic for Terry Today?


from Sub_Parsers import *
from Parser_Utility import *

class Variable_Sized_Graphic:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(visual_order_elements):

        elements = ['Visual Order:','X Origin:','Y Origin:','X Size:','Y Size:',
            'Refresh Affected Graphics Online?',
            'Enable Conditional Visibility?','Visibility Expression:',
            'Control Arrow Direction:','Control Arrow Display Flag:',
            'Alarm Device Name:']
        
        control_definitions = ['Control #','Control Label','Foreground Color',
                                'Background Color','PLC Bit Reference']

        graphic_states = ['State #','Symbol Name','Alarm','Alarm Ack','Foreground Color',
                          'Background Color','Conditional Expression']

        #split between base elements(non tabled), Control Definitions and Grapic States 
        visual_orders = {}
        for visual_order_element in visual_order_elements: #base element list is made up of everything before the Control Definitions Line
            base_elements_raw = visual_order_element[:visual_order_element.index('Control Definitions\n')]

            # Control Definitions are made up of everything after the Control Definitions line but before the Graphic States line
            control_definitions_raw = visual_order_element[visual_order_element.index('Control Definitions\n') + 1:
                                                        visual_order_element.index('Graphic States\n')]
        
            # Graphic States are made up of everthing after the Graphic States line to the end of the Visual Order list
            graphic_states_raw = visual_order_element[visual_order_element.index('Graphic States\n') + 1:]

#FIXME: For Gods sake, functionalize this unholy mess you're about to write! 
#FIXME: Maybe we don't need to copy elements to elements_working? I dunno, for cleanup later or something
            visual_order = {}
            elements_working = elements[:]
            for line in base_elements_raw: #Parse each Visual Order values

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
                            visual_order.update(parsed_element.get('element')) 
                            line = parsed_element.get('remaining_line')
                            elements_working.remove(member[1])
                            if not line.strip():
                                break


            #Logic for parsing control definition table FIXME: this is the crap I'm suppose to functionalize
            control_definition_table_raw = Parser_Utility.remove_table_headings(control_definitions, control_definitions_raw)

            control_definitions_table = {}

            for line in control_definition_table_raw:
                
                control_definition_elements = {}                
                
                index_modifier = 0
                #This voodoo should parse out anything in an element table
                for index, member in enumerate(control_definitions):  

                    index = index - index_modifier #to manipulate index for blank values

                    # Logic for control definition that does not have a Control label
                    if ((member == 'Control Label' or
                        member == 'PLC Bit Reference') and 
                        len(line.split(' ')) < 4):
                        parsed_element = { member : ''}
                        index_modifier += 1     #to not unsynch enumeration indexing while using the table_parser method

                    # Logic for a control definition with all columns filled 
                    #elif len(line.split(' ')) == 5:    
                    else:
                        parsed_element = Sub_Parsers.table_parser(member, index, line)

                    control_definition_elements.update(parsed_element)
                    
                    #make a dictionary of Control Definitions that houses Control #'s by their control number as a key...                
                control_definitions_table.update({ control_definition_elements['Control #'] : control_definition_elements })
            
            visual_order.update({ 'Control Definitions' : control_definitions_table }) 

            #Logic for parsing graphic state table FIXME: this is the crap I'm suppose to functionalize
            graphic_state_table_raw = Parser_Utility.remove_table_headings(graphic_states, graphic_states_raw)

            graphic_states_table = {}

            for line in graphic_state_table_raw:
                
                graphic_state_elements = {}                
                
                index_modifier = 0
                #This voodoo should parse out anything in an element table
                for index, member in enumerate(graphic_states):  

                    index = index - index_modifier #to manipulate index for blank values

                    # Logic for control definition that does not have a Control label
                    if ((member == 'Symbol Name' or
                        member == 'Conditional Expression') and 
                        len(line.split(' ')) < 6):
                        parsed_element = { member : ''}
                        index_modifier += 1     #to not unsynch enumeration indexing while using the table_parser method

                    # Logic for a control definition with all columns filled 
                    #elif len(line.split(' ')) == 5:    
                    else:
                        parsed_element = Sub_Parsers.table_parser(member, index, line)

                    graphic_state_elements.update(parsed_element)
                    
                    #make a dictionary of Control Definitions that houses Control #'s by their control number as a key...                
                graphic_states_table.update({ graphic_state_elements['State #'] : graphic_state_elements })
            
            visual_order.update({ 'Graphic States' : graphic_states_table })

            #Create dictionary of all Variable-Sized Grapic Templates Visual Order elements         
            visual_orders.update({visual_order['Visual Order'] : visual_order}) #wow, thats a confusing line!

        return visual_orders