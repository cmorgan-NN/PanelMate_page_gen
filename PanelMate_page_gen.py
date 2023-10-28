# Title: PanelMate_page_gen
# Author: C☩M
# Company: National Nonwovens
# Program Summary: Generates PanelMate Pro hmi page python programs which in turn render said hmi page 
# Date: October 24ᵗʰ - ?, Two Thousand Twenty Three Anno Domini

####################### 
# Theory of Operation #
#######################
# Take a directory full of Raw PanelMate Configurations files, which are different sections of a panelmate configuration PDF copied
# and pasted into a file with an extension of .rpc, as an input and create a python program that generates a rendered PanelMate HMI Page graphical output
# 1. parse each RPC as a seperate dictionary nested within a main page dictionary (name derived from top level directory)
# 2. Iterate through each nested dictionary, rendering the textual python code to a .py file

# Tree View of inputs:
# Top_Level_Directory (HMI Page name is derived from this)
# Top_Level_Directory/
# Top_Level_Directory/Static_Grapic_Data_Line_Elements.rpc
# Top_Level_Directory/Static_Grapic_Data_Rectangle_Elements.rpc
# Top_Level_Directory/Static_Grapic_Data_Text_Elements.rpc
# Top_Level_Directory/Variable-Sized_Indicator_Template.rpc
# Top_Level_Directory/Variable-Sized_Readout_Template.rpc
# Top_Level_Directory/Variable-Sized_Graphic_Template.rpc
# Top_Level_Directory/Variable-Sized_Control_Button_Template.rpc

#TODO:-[ ]- create Static_Grapic_Data_Line_Elements.rpc parser
#TODO:-[ ]- create Static_Grapic_Data_Rectangle_Elements.rpc parser
#TODO:-[ ]- create Static_Grapic_Data_Text_Elements.rpc parser
#TODO:-[X]- create Variable-Sized_Indicator_Template.rpc parser
#TODO:-[X]- create Variable-Sized_Readout_Template.rpc parser
#TODO:-[ ]- create Variable-Sized_Graphic_Template.rpc parser
#TODO:-[ ]- create Variable-Sized_Control_Button_Template.rpc parser

#########
# Begin #
#########

###########
# Imports #
###########

import sys
import os.path

#############
# Functions #
#############

###################
# File Operations #
###################

#handle cli stuff
cliArgumentNumber = len(sys.argv)
helpMessage = "Please enter the directory name where the PanelMate Page CSV files are located..."

if (cliArgumentNumber < 2):
    raise Exception(helpMessage)
    exit()
elif (cliArgumentNumber > 2):
    raise Exception("PanalMate_page_gen only accepts 1 argument. " + helpMessage)
    exit()
else:
    pageName = sys.argv[1]
    pageDir = pageName

# Confirm directory exists
if (not os.path.isdir(pageDir)):
    raise Exception("Directory not found. " + helpMessage)
else:
    print(pageDir, "directory found! This will be the name of the HMI page render file.")
    pageFile = (os.path.join(pageDir,pageDir + ".py"))

# Check if rendered page exists, if so, ask for overwrite
if (os.path.isfile(pageFile)):
    while (1):
        fileExistsYorN = input(pageFile + " exists. Overwrite? (Y/N):")
        if (fileExistsYorN.lower().strip() == 'y'):
            print("Overwriting", pageFile)
            break
        elif (fileExistsYorN.lower().strip() == 'n'):
            print("Please choose a new page directory and try again")
            exit(0)

else: #rendered py file does not exist
    print 
    with open(pageFile, 'w') as pageFilePy_file:
        pageFilePy_file.write('test')

#########
# Parse #
#########

# Make sure to reorder the VOs 


########## 
# Render #
##########

from pydraw import *

###############################
# Render Function Definitions #
###############################

# create functions for rendering each different type of VO

# Function for changing panelmate report colors (aka 'pen colors') 
#   to standard 24-bit/HTML colors
# See PanelMate Power Pro Manual for colors by pallete. 
#   This section is not comprehensive!
def panelMateColorTo24Bit(panelMateColor):
    panelMatePalette = ['#000000', '#0000ff', '#00ff00', '#00ffff', 
                        '#ff0000', '#ff00ff', '#ffff00', '#ffffff',
                        '#000000', '#0000ff', '#00ff00', '#00ffff', 
                        '#ff0000', '#ff00ff', '#ffff00', '#ffffff',
                        '#000000', '#808080', '#c0c0c0', '#ffffff', 
                        '#000000', '#808080', '#c0c0c0', '#ffffff']
    if (panelMateColor == 255):
        return '#FFFFFF'
    elif (panelMateColor <= 24):
        return panelMatePalette[panelMateColor]
    else:
        return '#000000'


######################
# Variables Renderer #
######################

# Render Screen
screen = Screen(640, 480, pageName)
screen.color(Color(panelMateColorTo24Bit(0)))

# Render plcReferences dictionary
plcReferences = { #GE Fanuc Reference Python Dictionary

    #Output Coils
    '%Q0056' : False,

    #Discrete Internal Coils, %M in GE Fanuc PLC
    '%M0031' : False,
    '%M0032' : False,
    '%M0033' : False,
    '%M0034' : False,
    '%M0035' : False,
    '%M0810' : False,
    '%M0811' : False,
    '%M0812' : False,

    #Registers, %R in GE Fanuc PLC
    
    '%R0102' : '[R0102]', #output divided by 10 on HMI
    '%R0104' : '[R0104]', #output divided by 10 on HMI
    '%R0109' : '[R0109]', #output divided by 10 on HMI
    '%R0111' : '[R0111]', #output divided by 10 on HMI
    '%R0114' : '[R0114]', #output divided by 10 on HMI
    '%R0115' : '[R0115]'  #output divided by 10 on HMI
}

#############################
# Render Page Visual Orders #
#############################

# depending on what current VO is, then call appropriate renderer for that VO and render to python source


############################
# Render final PyDraw code #
############################
# To be rendered to py file
# fps = 30
# running = True
# while running:
#     screen.update()
#     screen.sleep(1 / fps)
#     if (screen.size() == (-1, -1)): # exit when screen closes
#         break