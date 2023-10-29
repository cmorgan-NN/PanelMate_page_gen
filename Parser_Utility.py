#Utility functions common to all parsers

class Parser_Utility:
    # Function to remove page breaks from PanelMate 
    #   preprocessed Variable-Sized_Indicator_Template report elements 
    def remove_page_breaks(rpc_data):
        #find page breaks
        line_number = 0
        page_break_lines = []
        for line in rpc_data:
            line_number += 1
            if 'Page' and 'Configuration' in line: #the page line contains Page and Configuration
                page_break_lines.append(line_number - 1) #the line before a page line is unwanted
                page_break_lines.append(line_number)
                page_break_lines.append(line_number + 1) #and the line after a page line is unwanted

        #create a new list of data without page breaks
        line_number = 0
        rpc_data_file_lines = []
        for line in rpc_data:
            line_number += 1
            if line_number not in page_break_lines:
                rpc_data_file_lines.append(line)

        #passback data
        return rpc_data_file_lines


    # Function to seperate visual orders and return list
    def seperate_visual_orders(rpc_data_file_lines):
        visual_orders = []
        visual_order = []
        line_number = 0

        #determines if new list item should be made and appends line
        for line in rpc_data_file_lines:
            
            line_number += 1
            
            #seperate VOs
            if line.find('Visual Order: ') != -1:
                if visual_order: #if list is populated (needed for first VO)
                    visual_orders.append(visual_order.copy())
                visual_order.clear()
                
            visual_order.append(line)

            #if line is last line
            if line_number == len(rpc_data_file_lines):
                visual_orders.append(visual_order.copy())
                
        return visual_orders
    
    def remove_table_headings(headings, table_data):
        
        split_headings = []

        for heading in headings: 
            split_headings.extend(heading.split(' '))
        
        for heading in split_headings:
            line_number = 0
            for line in table_data:
                if line.find(heading) > -1:
                    del(table_data[line_number])
                line_number += 1
        
        return table_data