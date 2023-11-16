# Title: PanelMate_page_gen
# Author: C☩M
# Company: National Nonwovens
# Program Summary: Generates PanelMate Pro hmi page python programs which in turn render said hmi page 
# Date: October 24ᵗʰ - ?, Two Thousand Twenty Three Anno Domini

####################### 
# Theory of Operation #
#######################
# Take a directory full of Raw PanelMate Configurations files, which are different sections of a panelmate configuration 
# PDF copied and pasted into a file with an extension of .rpc, as an input and create a python program that generates a 
# rendered PanelMate HMI Page graphical output
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

# Copilot's explaination of the program to me:
# GitHub Copilot: Your program appears to be a graphical user interface (GUI) for a
# system, possibly related to controlling drives. It uses the `pydraw` library 
# to create a screen and display text elements on it. 
# The text elements include "EXIT", "PAGE UP", and "DRIVE", 
# suggesting some form of navigation or control panel. 
# The function `panelMateColorTo24Bit` is used to convert 
# PanelMate color codes to standard 24-bit/HTML color codes, 
# which are then used to set the color of the text elements.

# My explaination of the program to Copilot:
# You were close. This program renders what a gui page from parts of an 
# obsolete HMI panel's configuration report looks like in order to help 
# an engineer or tech analyse which PLC references, or tags, are used to 
# communicate between said HMI and any PLCs it is connected to.

################
# Global TODOs #
################

# TODO: change all renderers to us vo_type_string variable instead of hard coded strings
# by passing vo_type through
# FIXME: reference coils not showing up for VS Control Buttons

#########
# Begin #
#########

###########
# Imports #
###########

import sys
import os.path
import winsound
from Parser import *
from Renderer import *

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

def render_plc_references(plc_reference, rendered_references):
    #function to render plc references to the rendered_references list
    if plc_reference[:2] == '%Q':
        rendered_references.extend(["    '" + plc_reference + 
                                   "' : False,"])
    elif plc_reference[:2] == '%M':
        rendered_references.extend(["    '" + plc_reference + 
                                   "' : False,"])
    elif plc_reference[:2] == '%R':
        rendered_references.extend(["    '" + plc_reference + 
                                   "' : '["+ +"'],"])
    return rendered_references

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

#########
# Parse #
#########
#TODO: maybe make this a method with input of pageDir and output of top_level_dictionary
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

# page file render parts
rendered_begining = []
rendered_functions = []
rendered_variables = []
q_references = []
m_references = []
r_references = []
rendered_draw_data = []
rendered_end = []

temporary_rendered_references = []


#######################
# Render Dependancies #
#######################

rendered_begining.append('from pydraw import *')


###############################
# Render Function Definitions #
###############################

rendered_functions.extend([
    "",
    "# Function for changing panelmate report colors (aka 'pen colors') ",
    "#   to standard 24-bit/HTML colors",
    "# See PanelMate Power Pro Manual for colors by pallete. ",
    "#   This section is not comprehensive!",
    "def panelMateColorTo24Bit(panelMateColor):",
    "    panelMatePalette = ['#000000', '#0000ff', '#00ff00', '#00ffff', ",
    "                        '#ff0000', '#ff00ff', '#ffff00', '#ffffff',",
    "                        '#000000', '#0000ff', '#00ff00', '#00ffff', ",
    "                        '#ff0000', '#ff00ff', '#ffff00', '#ffffff',",
    "                        '#000000', '#808080', '#c0c0c0', '#ffffff', ",
    "                        '#000000', '#808080', '#c0c0c0', '#ffffff']",
    "    if (panelMateColor == 255):",
    "        return '#FFFFFF'",
    "    elif (panelMateColor <= 24):",
    "        return panelMatePalette[panelMateColor]",
    "    else:",
    "        return '#000000'",
    ""])


####################
# Render Variables #
####################

rendered_variables.extend(["screen = Screen(640, 480, 'Page: " + pageDir + "')",
                    "screen.color(Color(panelMateColorTo24Bit(0)))",
                    ""])


###############################################
# Generate Render Data for Page Visual Orders #
###############################################
# make lists of vo's in elements

#cycling through all visual orders, in order and removing them from top_level_directory afterwards
remove = ''
while top_level_dictionary:
    #remove becomes non empty (true) when below "if not" detects that the element_type sub dictionary
    #
    if remove:
        top_level_dictionary.pop(remove)
        remove = ''
    for element_type in top_level_dictionary:
        if not top_level_dictionary[element_type]:  #the aforementioned "if not" that triggers removal of the empty sub element
            remove = element_type
            break 
        else:
            vo_to_render, top_level_dictionary = lowest_visual_order(top_level_dictionary)

        current_vo_type = list(vo_to_render.keys())[0] #getting the type for the current visual order

        # start rendering different types of visual orders
        if current_vo_type == 'lines':        
            rendered_draw_data.extend(Render.static_grapic_data_line(vo_to_render[current_vo_type]))

        elif current_vo_type == 'rectangles':
            rendered_draw_data.extend(Render.static_graphic_data_rectangle(vo_to_render[current_vo_type]))
        
        elif current_vo_type == 'text':

            rendered_draw_data_text, rendered_reference = Render.static_graphic_data_text(vo_to_render[current_vo_type])
            
            rendered_draw_data.extend(rendered_draw_data_text)

            #avoid duplicates and blanks in references with if
            if (rendered_reference not in temporary_rendered_references and
                rendered_reference != []): 
                temporary_rendered_references.extend([rendered_reference])

#        
#    elif current_vo_type == 'indicator':
#        screen_file.extend(Render.variable_sized_indicator(vo_to_render[current_vo_type]))
#        
        elif current_vo_type == 'readout':
            
            rendered_draw_data_readout, rendered_reference = Render.variable_sized_readout(vo_to_render[current_vo_type])
        
            
        elif current_vo_type == 'control_button':

            rendered_draw_data_control_button, rendered_reference = Render.variable_sized_control_button(vo_to_render[current_vo_type])

            rendered_draw_data.extend(rendered_draw_data_control_button)

            #avoid duplicates and blanks in references with if
            if (rendered_reference not in temporary_rendered_references and
                rendered_reference != []): 
                temporary_rendered_references.extend([rendered_reference]) #FIXME: It's passing back extra blanks in rendered_reference
#        
#    elif current_vo_type == 'graphic':
#        screen_file.extend(Render.variable_sized_graphic(vo_to_render[current_vo_type]))

#########################           
# Render Plc References #
#########################
#TODO: make this a method with input of temporary_rendered_references
#      and output of rendered_referencecs

rendered_references = []
if temporary_rendered_references:
    for plc_reference in temporary_rendered_references:
        for instance in plc_reference:
            
            if instance[:2] == '%Q':
                q_references.extend(["    '" + instance + 
                                    "' : False,"])

            elif instance[:2] == '%M':
                m_references.extend(["    '" + instance + 
                                    "' : False,"])

            elif instance[:2] == '%R':
                r_references.extend(["    '" + instance + 
                                    "' : '["+ instance +"'],"])


    #render plc reference dictionary initialization
    rendered_references.extend(['plc_references = {',''])

    #render heading comments before references
    #NOTE: tried to do this more eligantly with a one liner but python didn't like:
    #      ["#Output Coils (%Q in GE Fanuc PLC)"].extend(q_references.copy())
    if q_references: 
        q_references_p = ['    #Output Coils (%Q in GE Fanuc PLC)']
        q_references_p.extend(q_references)
        q_references = q_references_p.copy()
        q_references.extend([''])
        rendered_references.extend(q_references)

    if m_references: 
        m_references_p = ['    #Internal Coils (%M in GE Fanuc PLC)']
        m_references_p.extend(m_references)
        m_references = m_references_p.copy()
        m_references.extend([''])
        rendered_references.extend(m_references)
    
    if r_references: 
        r_references_p = ["    #Registers (%R in GE Fanuc PLC)"]
        r_references_p.extend(r_references)
        r_references = r_references_p.copy()
        r_references.extend([''])
        rendered_references.extend(r_references)  
    
    # remove trailing comma from last reference
    rendered_references[-2] = rendered_references[-2].rstrip(',')
    
    #render closing bracket
    rendered_references.extend(['}',''])
            

#############################
## Render final PyDraw code #
#############################
rendered_end.extend(["fps = 30",
                    "running = True",
                    "while running:",
                    "    screen.update()",
                    "    screen.sleep(1 / fps)",
                    "    if (screen.size() == (-1, -1)): # exit when screen closes",
                    "        break"])

###############
# Render Page #
###############
# page 
rendered_page = [rendered_begining,
                 rendered_functions,
                 rendered_variables,
                 rendered_references,
                 rendered_draw_data,
                 rendered_end]

with open (pageFile, 'w') as pageFilePy_file:
    for section in rendered_page:
        for line in section:
            pageFilePy_file.writelines(line + "\n")

winsound.Beep(440, 500)