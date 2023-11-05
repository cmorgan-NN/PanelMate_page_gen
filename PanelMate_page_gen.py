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

#TODO:-[X]- create Static_Grapic_Data_Line_Elements.rpc parser
#TODO:-[X]- create Static_Grapic_Data_Rectangle_Elements.rpc parser
#TODO:-[X]- create Static_Grapic_Data_Text_Elements.rpc parser
#TODO:-[X]- create Variable-Sized_Indicator_Template.rpc parser
#TODO:-[X]- create Variable-Sized_Readout_Template.rpc parser
#TODO:-[X]- create Variable-Sized_Graphic_Template.rpc parser
#TODO:-[X]- create Variable-Sized_Control_Button_Template.rpc parser

#########
# Begin #
#########

###########
# Imports #
###########

import sys
import os.path
import json
from Parser import *

#############
# Functions #
#############

# Function with input of top_level_dictionary and
# return lowest visual order tuple: 
#  (lowest_vo dict entry, top_level_directory with lowest vo removed) 

# find current lowest visual order
def lowest_visual_order(top_level_dictionary):

    highest_visual_order = 1
    #find highest
    for element_type in top_level_dictionary:
        element_vos = []
        element_vos_list = list(top_level_dictionary[element_type].keys())
        for vo in element_vos_list:
            element_vos.append(int(vo))
        
        if element_vos:
            if highest_visual_order < max(element_vos):
                highest_visual_order = max(element_vos)

    lowest_visual_order = highest_visual_order
    # peel off lowest and return
    for element_type in top_level_dictionary:

        element_vos = []

        #find all vo numbers
        element_vos_list = list(top_level_dictionary[element_type].keys())

        #cast to list for comparisons
        for vo in element_vos_list:
            element_vos.append(int(vo))

        #find lowest vo and create a tuple (visual_order, element_type)
        if element_vos: #if list not empty
            if min(element_vos) <= highest_visual_order:
                if lowest_visual_order >= min(element_vos):
                    lowest_visual_order = min(element_vos)
                    lowest_vo_element_type_return = element_type
    
    lowest_visual_order_return = top_level_dictionary[lowest_vo_element_type_return].pop(str(lowest_visual_order))       
    return_element = { lowest_vo_element_type_return : lowest_visual_order_return }     
    return ((return_element, top_level_dictionary))

###################
# File Operations #
###################

#handle cli stuff
cliArgumentNumber = len(sys.argv)
helpMessage = "Please enter the directory name where the PanelMate Page .rpc files are located..."

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
    pageFile = (os.path.join(pageDir,pageDir + ".json"))

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

#########
# Parse #
#########

top_level_dictionary = {}
rpc_files_to_parse = []

#make directory list
for file in os.listdir(pageDir):
    if file[len(file) - 4:].lower() == '.rpc':
        rpc_files_to_parse.append(file)

for file in rpc_files_to_parse:
    rpc_file = pageDir + '\\' + file

    if file == 'Static_Graphic_Data_Line_Elements.rpc':
        if 'lines' not in top_level_dictionary:
            top_level_dictionary.update({ 'lines' : {} })
        parsed_static_graphic_data_line = Parser.static_graphic_data_line(rpc_file)
        top_level_dictionary['lines'].update(parsed_static_graphic_data_line)
        
    elif file == 'Static_Graphic_Data_Rectangle_Elements.rpc':
        if 'rectangles' not in top_level_dictionary:
            top_level_dictionary.update({ 'rectangles' : {} })
        parsed_static_graphic_data_rectangle = Parser.static_graphic_data_rectangle(rpc_file)
        top_level_dictionary['rectangles'].update(parsed_static_graphic_data_rectangle)

    elif file == 'Static_Graphic_Data_Text_Elements.rpc':
        if 'text' not in top_level_dictionary:
            top_level_dictionary.update({ 'text' : {} })
        parsed_static_graphic_data_text = Parser.static_graphic_data_text(rpc_file)
        top_level_dictionary['text'].update(parsed_static_graphic_data_text)

    elif file == 'Variable-Sized_Indicator_Template.rpc':
        if 'indicator' not in top_level_dictionary:
            top_level_dictionary.update({ 'indicator' : {} })
        parsed_inicator = Parser.variable_sized_indicator(rpc_file)
        top_level_dictionary['indicator'].update(parsed_inicator)

    elif file == 'Variable-Sized_Readout_Template.rpc':
        if 'readout' not in top_level_dictionary:
            top_level_dictionary.update({ 'readout' : {} })
        parsed_readout = Parser.variable_sized_readout(rpc_file)
        top_level_dictionary['readout'].update(parsed_readout)

    elif file == 'Variable-Sized_Control_Button_Template.rpc':
        if 'control_button' not in top_level_dictionary:
            top_level_dictionary.update({ 'control_button' : {} })
        parsed_control_button = Parser.variable_sized_control_button(rpc_file)
        top_level_dictionary['control_button'].update(parsed_control_button)

    elif file == 'Variable-Sized_Graphic_Template.rpc':
        if 'graphic' not in top_level_dictionary:
            top_level_dictionary.update({ 'graphic' : {} })
        parsed_graphic = Parser.variable_sized_graphic(rpc_file)
        top_level_dictionary['graphic'].update(parsed_graphic)

############## 
# Pre Render #
##############

#cycling through all visual orders, in order and removing them from top_level_directory afterwards
remove = ''

with open (pageFile, 'w') as pageFilePy_file:
#    while top_level_dictionary:
#        #remove becomes non empty (true) when below "if not" detects that the element_type sub dictionary
#        #
#        if remove:
#            top_level_dictionary.pop(remove)
#            remove = ''
#        for element_type in top_level_dictionary:
#            if not top_level_dictionary[element_type]:  #the aforementioned "if not" that triggers removal of the empty sub element
#                remove = element_type
#                break 
#            else:
#                vo_to_render, top_level_dictionary = lowest_visual_order(top_level_dictionary)
    json.dump(top_level_dictionary, pageFilePy_file)
                
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

###############################################
# Generate Render Data for Page Visual Orders #
###############################################
# make lists of vo's in elements

# Create a dictionary with the visual order number as the key and a list of python code as the value
rendered_static_graphic_data_line = Render.static_grapic_data_line(parsed_static_graphic_data_line)

rendered_static_graphic_data_rectangle = Render.static_graphic_data_rectangle(parsed_static_graphic_data_rectangle)

rendered_static_graphic_data_text = Render.static_graphic_data_text(parsed_static_graphic_data_text)

rendered_inicator = Render.variable_sized_indicator(parsed_inicator)

rendered_readout = Render.variable_sized_readout(parsed_readout)

rendered_control_button = Render.variable_sized_control_button()

rendered_graphic = Render.variable_sized_graphic()

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