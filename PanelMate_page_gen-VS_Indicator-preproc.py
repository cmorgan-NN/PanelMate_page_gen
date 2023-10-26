# Preprocessor for Variable-Sized_Indicator_Template 
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

############# 
# Functions #
#############

# Function to remove page breaks from PanelMate 
#   preprocessed Variable-Sized_Indicator_Template report elements 
def removePageBreaks(preprocessedVS_IndicatorFileLines_Raw):
    #find page breaks
    lineNumber = 0
    pageBreakLines = []
    for line in preprocessedVS_IndicatorFileLines_Raw:
        lineNumber += 1
        if "Page" and "Configuration" in line: #the page line contains Page and Configuration
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
def seperateVSIndicatorVOs(preprocessedVS_IndicatorFileLines):
    VSIndicatorVOs = []
    VSIndicatorVO= []
    lineNumber = 0
    
    for line in preprocessedVS_IndicatorFileLines:# A Visual Order is always 13 lines long
        lineNumber += 1
        VSIndicatorVO.append(line) 
        if (lineNumber == 13):     
            lineNumber = 0
            VSIndicatorVOs.append(VSIndicatorVO.copy())
            VSIndicatorVO.clear()
    
    return VSIndicatorVOs


#########
# Begin #
#########

###################
# Filesystem Read #
###################

# TODO Add filesystem stuff to make this dynamic or passed from page_gen parent  

# Read in lines of preprocessed file
preprocessedVS_IndicatorFilename = "Gas Alarms\Variable-Sized_Indicator_Template.pre"
preprocessedVS_IndicatorFile = open(preprocessedVS_IndicatorFilename, 'r')
preprocessedVS_IndicatorFileLines_Raw = preprocessedVS_IndicatorFile.readlines()

# remove page breaks
preprocessedVS_IndicatorFileLines = removePageBreaks(preprocessedVS_IndicatorFileLines_Raw)

# seperate Visual Orders
visualOrderElementsList = seperateVSIndicatorVOs(preprocessedVS_IndicatorFileLines)

# TODO function to extract data
visualOrders = {}
entryNumber = 0
for VO in visualOrderElementsList:
    entryNumber += 1
    visualOrder = {}
    for line in VO:
        if (line.find('Visual Order: ') == 0): 
            vODictKey = line.lstrip('Visual Order: ') #extract "Visual Order: "
            print (vODictKey)
            vODictVal = line[0:(line.find(' ') - 1)]  #extract VO value
            print (vODictVal)
            visualOrder.update({vODictKey : vODictVal}) #store both extracteds to VO dictitonary entry
            line.lstrip(' ')
        #    exit()
print(visualOrder)
# TODO function to render dictionary of Visual Order dictionaries 

