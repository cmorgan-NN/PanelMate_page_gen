#Utility functions common to all parsers

class Parser_Utility:
    # Function to remove page breaks from PanelMate 
    #   preprocessed Variable-Sized_Indicator_Template report elements 
    def remove_page_breaks(preprocessedVS_IndicatorFileLines_Raw):
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
    def seperate_visual_orders(preprocessedVS_IndicatorFileLines):
        VOs = []
        VO = []
        line_number = 0

        #determines if new list item should be made and appends line
        for line in preprocessedVS_IndicatorFileLines:
            
            line_number += 1
            
            #seperate VOs
            if line.find('Visual Order: ') != -1:
                if VO: #if list is populated (needed for first VO)
                    VOs.append(VO.copy())
                VO.clear()
                
            VO.append(line)

            #if line is last line
            if line_number == len(preprocessedVS_IndicatorFileLines):
                VOs.append(VO.copy())
                
        return VOs
    
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