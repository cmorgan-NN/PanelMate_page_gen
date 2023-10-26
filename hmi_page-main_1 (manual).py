# Title: hmi_page_gen
# Author: C☩M
# Company: National Nonwovens
# Program Summary: PanelMate Pro HMI Page Generator
# Date: October 19ᵗʰ - ?, Two Thousand Twenty Three Anno Domini

########### 
# Imports #
###########

from pydraw import *

########################
# Function Definitions #
########################

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

#############
# Variables #
#############

screen = Screen(640, 480, 'Conveyor Dryer: Main 1')
screen.color(Color(panelMateColorTo24Bit(0)))


plcReference = { #GE Fanuc Reference Python Dictionary

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

##############################
# Visual Orders to draw here #
##############################

# Rectangles are n-1 to account for their borders
#Visual Order 1 
rectangleEl1 = Rectangle(screen, 1, 120, 104-1, 135-1)  # ouput dev, X, Y, Width, Height
rectangleEl1.color(Color(panelMateColorTo24Bit(18)))    # fill color 
rectangleEl1.border(Color(panelMateColorTo24Bit(7)))    # Pen color
rectangleEl1.border_width(1)                            # Pen Width (in px)

#Visual Order 2 (Visibility Conditional)
textEl2 = Text(screen, 'DRIVE NOT',  17, 205)
textEl2.color(Color(panelMateColorTo24Bit(7)))
textEl2.size(12)
textEl2.visible(plcReference['%M0031'])

#Visual Order 3 (Visibility Conditional)
textEl3 = Text(screen, 'ENABLED',  25, 221)
textEl3.color(Color(panelMateColorTo24Bit(7)))
textEl3.size(12)
textEl3.visible(plcReference['%M0031'])

#Visual Order 4 (Page Change to 14)
conButtonEl4 = Rectangle(screen, 448, 369, 75, 48)
conButtonEl4.color(Color(panelMateColorTo24Bit(18)))
conButtonEl4.border(Color(panelMateColorTo24Bit(0)))
conButtonEl4.border_width(1)
conButtonEl4.back()

#Visual Order 5
textEl5 = Text(screen, 'NEXT', 470, 374)
textEl5.color(Color(panelMateColorTo24Bit(0)))
textEl5.size(12)

#Visual Order 6
textEl6 = Text(screen, 'PAGE', 470, 392)
textEl6.color(Color(panelMateColorTo24Bit(0)))
textEl6.size(12)

#Visual Order 7
textEl7 = Text(screen, 'LINE', 132, 388)
textEl7.color(Color(panelMateColorTo24Bit(3)))
textEl7.size(12)

#Visual Order 8
textEl8 = Text(screen, 'SPEED', 129, 403)
textEl8.color(Color(panelMateColorTo24Bit(3)))
textEl8.size(12)

#Visual Order 9
rectangleEl9 = Rectangle(screen, 108, 422, 78-1, 32-1)
rectangleEl9.color(Color(panelMateColorTo24Bit(8))) 
rectangleEl9.border(Color(panelMateColorTo24Bit(17)))
rectangleEl9.border_width(1)

#Visual Order 10
textEl10 = Text(screen, 'YPM', 156, 431)
textEl10.color(Color(panelMateColorTo24Bit(2)))
textEl10.size(12)

#Visual Order 11
readOutEl11 = Text(screen, plcReference['%R0114'], 115, 430) # output dev, text to display (using plcReference dictionary, see variables), X origin, Y origin
readOutEl11.color(Color(panelMateColorTo24Bit(2)))           # Pen Color (in px)
readOutEl11.size(10)                                         # Font size (adjust by eye, atm)

#Visual Order 12
lineEl12 = Line(screen, 111, 423, 183, 423)             # output dev, X origin, Y origin, X end, Y end            
lineEl12.thickness(2)                                   # Pen Width (in px)
lineEl12.color(Color(panelMateColorTo24Bit(7)))         # Pen Color

#Visual Order 13
lineEl13 = Line(screen, 110, 423, 110, 452)                         
lineEl13.thickness(2)                                   
lineEl13.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 14
lineEl14 = Line(screen, 164, 422, 182, 422)                         
lineEl14.thickness(1)                                   
lineEl14.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 15
rectangleEl15 = Rectangle(screen, 102, 382, 90-1, 80-1)
rectangleEl15.color(Color(panelMateColorTo24Bit(255))) 
rectangleEl15.border(Color(panelMateColorTo24Bit(7)))
rectangleEl15.border_width(1)
rectangleEl15.back()                                    # Move to back

#Visual Order 16 (Page Change to 13)
conButtonEl16 = Rectangle(screen, 448, 416, 75, 48)
conButtonEl16.color(Color(panelMateColorTo24Bit(18)))
conButtonEl16.border(Color(panelMateColorTo24Bit(0)))
conButtonEl16.border_width(1)
conButtonEl16.back()

#Visual Order 17 (Page Change to 9)
conButtonEl17 = Rectangle(screen, 362, 416, 75, 48)
conButtonEl17.color(Color(panelMateColorTo24Bit(18)))
conButtonEl17.border(Color(panelMateColorTo24Bit(0)))
conButtonEl17.border_width(1)
conButtonEl17.back()

#Visual Order 18 (Page Change to 8)
conButtonEl18 = Rectangle(screen, 214, 416, 75, 48)
conButtonEl18.color(Color(panelMateColorTo24Bit(18)))
conButtonEl18.border(Color(panelMateColorTo24Bit(0)))
conButtonEl18.border_width(1)
conButtonEl18.back()

#Visual Order 19 (Page Change to 6)
conButtonEl19 = Rectangle(screen, 288, 416, 75, 48)
conButtonEl19.color(Color(panelMateColorTo24Bit(18)))
conButtonEl19.border(Color(panelMateColorTo24Bit(0)))
conButtonEl19.border_width(1)
conButtonEl19.back()

#Visual Order 20
textEl20 = Text(screen, 'EXHAUST', 225, 421)
textEl20.color(Color(panelMateColorTo24Bit(0)))
textEl20.size(12)

#Visual Order 21
textEl21 = Text(screen, 'CIRC.', 307, 420)
textEl21.color(Color(panelMateColorTo24Bit(0)))
textEl21.size(12)

#Visual Order 22
textEl22 = Text(screen, 'FANS', 309, 439)
textEl22.color(Color(panelMateColorTo24Bit(0)))
textEl22.size(12)

#Visual Order 23
textEl23 = Text(screen, 'FAN', 237, 438)
textEl23.color(Color(panelMateColorTo24Bit(0)))
textEl23.size(12)

#Visual Order 24
textEl24 = Text(screen, 'BURNER', 375, 421)
textEl24.color(Color(panelMateColorTo24Bit(0)))
textEl24.size(12)

#Visual Order 25
textEl25 = Text(screen, 'CONTROL', 373, 438)
textEl25.color(Color(panelMateColorTo24Bit(0)))
textEl25.size(12)

#Visual Order 26 (Page Change to 100)
conButtonEl26 = Rectangle(screen, 288, 369, 75, 48)
conButtonEl26.color(Color(panelMateColorTo24Bit(18)))
conButtonEl26.border(Color(panelMateColorTo24Bit(0)))
conButtonEl26.border_width(1)
conButtonEl26.back()

#Visual Order 27
textEl27 = Text(screen, 'LINE', 469, 421)
textEl27.color(Color(panelMateColorTo24Bit(0)))
textEl27.size(12)

#Visual Order 28
textEl28 = Text(screen, 'SPEED', 466, 439)
textEl28.color(Color(panelMateColorTo24Bit(0)))
textEl28.size(12)

#Visual Order 29
textEl29 = Text(screen, 'ALARMS', 302, 383)
textEl29.color(Color(panelMateColorTo24Bit(0)))
textEl29.size(12)

#Visual Order 30 (Normally On Momentary: [%M0988])                    
conButtonEl30 = Rectangle(screen, 362, 369, 75, 48)
conButtonEl30.color(Color(panelMateColorTo24Bit(18)))
conButtonEl30.border(Color(panelMateColorTo24Bit(0)))
conButtonEl30.border_width(1)
conButtonEl30.back()

#Visual Order 31
textEl31 = Text(screen, 'ALARM', 379, 375)
textEl31.color(Color(panelMateColorTo24Bit(0)))
textEl31.size(12)

#Visual Order 32
textEl32 = Text(screen, 'RESET', 379, 389)
textEl32.color(Color(panelMateColorTo24Bit(0)))
textEl32.size(12)

#Visual Order 33
rectangleEl33 = Rectangle(screen, 421, 120, 104-1, 135-1)
rectangleEl33.color(Color(panelMateColorTo24Bit(18))) 
rectangleEl33.border(Color(panelMateColorTo24Bit(7)))
rectangleEl33.border_width(1)

#Visual Order 34
rectangleEl34 = Rectangle(screen, 433, 156,  78-1,  32-1)
rectangleEl34.color(Color(panelMateColorTo24Bit(8))) 
rectangleEl34.border(Color(panelMateColorTo24Bit(17)))
rectangleEl34.border_width(2)

#Visual Order 35
textEl35 = Text(screen, 'YPM', 481, 166)
textEl35.color(Color(panelMateColorTo24Bit(2)))
textEl35.size(12)

#Visual Order 36
readOutEl36 = Text(screen, plcReference['%R0109'], 442, 165)
readOutEl36.color(Color(panelMateColorTo24Bit(2)))
readOutEl36.size(10)

#Visual Order 37
lineEl37 = Line(screen, 436, 157, 508, 157)                         
lineEl37.thickness(2)                                   
lineEl37.color(Color(panelMateColorTo24Bit(7)))         


#Visual Order 38
lineEl38 = Line(screen, 434, 186, 434, 157)                         
lineEl38.thickness(2)                                   
lineEl38.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 39
textEl39 = Text(screen, 'FOLDER', 444, 124)
textEl39.color(Color(panelMateColorTo24Bit(0)))
textEl39.size(12)

#Visual Order 40
rectangleEl40 = Rectangle(screen, 13, 156,  78-1,  32-1)
rectangleEl40.color(Color(panelMateColorTo24Bit( 8))) 
rectangleEl40.border(Color(panelMateColorTo24Bit(17)))
rectangleEl40.border_width(2)

#Visual Order 41
textEl41 = Text(screen, 'YPM', 61, 165)
textEl41.color(Color(panelMateColorTo24Bit(2)))
textEl41.size(12)

#Visual Order 42
readOutEl42 = Text(screen, plcReference['%R0115'], 22, 165)
readOutEl42.color(Color(panelMateColorTo24Bit(2)))
readOutEl42.size(10)

#Visual Order 43
lineEl43 = Line(screen,  16, 157,  88, 157)                         
lineEl43.thickness(2)                                   
lineEl43.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 44
lineEl44 = Line(screen,  14, 186,  14, 157)                         
lineEl44.thickness(2)                                   
lineEl44.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 45
textEl45 = Text(screen, 'ENTRY PAD', 16, 124)
textEl45.color(Color(panelMateColorTo24Bit(0)))
textEl45.size(12)

#Visual Order 46 (Visibility Conditional)
textEl46 = Text(screen, 'IN AUTO',  25, 221)
textEl46.color(Color(panelMateColorTo24Bit(7)))
textEl46.size(12)
textEl46.visible(plcReference['%M0031'])

#Visual Order 47 (Visibility Conditional)
textEl47 = Text(screen, 'IN AUTO', 445, 221)
textEl47.color(Color(panelMateColorTo24Bit(7)))
textEl47.size(12)
textEl47.visible(plcReference['%M0035'])

#Visual Order 48 (Visibility Conditional)
textEl48 = Text(screen, 'DRIVE NOT',  437, 206)
textEl48.color(Color(panelMateColorTo24Bit(7)))
textEl48.size(12)
textEl48.visible(plcReference['%M0035'])

#Visual Order 51
rectangleEl51 = Rectangle(screen, 106, 120, 104-1, 135-1)
rectangleEl51.color(Color(panelMateColorTo24Bit(18))) 
rectangleEl51.border(Color(panelMateColorTo24Bit(7)))
rectangleEl51.border_width(1)

#Visual Order 52 (Visibility Conditional)
textEl52 = Text(screen, 'DRIVE NOT',  122, 206)
textEl52.color(Color(panelMateColorTo24Bit(7)))
textEl52.size(12)
textEl52.visible(plcReference['%M0032'])

#Visual Order 53
rectangleEl53 = Rectangle(screen, 118, 156,  78-1,  32-1)
rectangleEl53.color(Color(panelMateColorTo24Bit(8))) 
rectangleEl53.border(Color(panelMateColorTo24Bit(17)))
rectangleEl53.border_width(2)

#Visual Order 54
textEl54 = Text(screen, 'YPM', 166, 166)
textEl54.color(Color(panelMateColorTo24Bit(2)))
textEl54.size(12)

#Visual Order 55
readOutEl55 = Text(screen, plcReference['%R0111'], 127, 165)
readOutEl55.color(Color(panelMateColorTo24Bit(2)))
readOutEl55.size(10)

#Visual Order 56
lineEl56 = Line(screen, 121, 157, 193, 157)                         
lineEl56.thickness(2)                                   
lineEl56.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 57
lineEl57 = Line(screen, 119, 186, 119, 157)                         
lineEl57.thickness(2)                                   
lineEl57.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 58
lineEl58 = Line(screen, 148, 156, 166, 156)                         
lineEl58.thickness(1)                                   
lineEl58.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 59
textEl59 = Text(screen, 'STEAM ROLLS 1', 106, 124)
textEl59.color(Color(panelMateColorTo24Bit(0)))
textEl59.size(12)

#Visual Order 60 (Visibility Conditional)
textEl60 = Text(screen, 'IN AUTO', 130, 221)
textEl60.color(Color(panelMateColorTo24Bit(7)))
textEl60.size(12)
textEl60.visible(plcReference['%M0032'])

#Visual Order 62
rectangleEl62 = Rectangle(screen, 211, 120, 104-1, 135-1)
rectangleEl62.color(Color(panelMateColorTo24Bit(18))) 
rectangleEl62.border(Color(panelMateColorTo24Bit(7)))
rectangleEl62.border_width(1)

#Visual Order 63 (Visibility Conditional)
textEl63 = Text(screen, 'DRIVE NOT',  227, 206)
textEl63.color(Color(panelMateColorTo24Bit(7)))
textEl63.size(12)
textEl63.visible(plcReference['%M0033'])

#Visual Order 64
rectangleEl64 = Rectangle(screen, 223, 156,  78-1,  32-1)
rectangleEl64.color(Color(panelMateColorTo24Bit( 8))) 
rectangleEl64.border(Color(panelMateColorTo24Bit(17)))
rectangleEl64.border_width(2)

#Visual Order 65
textEl65 = Text(screen, 'YPM', 271, 166)
textEl65.color(Color(panelMateColorTo24Bit(2)))
textEl65.size(12)

#Visual Order 66
readOutEl66 = Text(screen, plcReference['%R0102'], 232, 165)
readOutEl66.color(Color(panelMateColorTo24Bit(2)))
readOutEl66.size(10)

#Visual Order 67
lineEl67 = Line(screen, 226, 157, 298, 157)                         
lineEl67.thickness(2)                                   
lineEl67.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 68
lineEl68 = Line(screen, 224, 186, 224, 157)                         
lineEl68.thickness(2)                                   
lineEl68.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 69
textEl69 = Text(screen, 'STEAM ROLLS 2', 211, 124)
textEl69.color(Color(panelMateColorTo24Bit(0)))
textEl69.size(12)

#Visual Order 70 (Visibility Conditional)
textEl70 = Text(screen, 'IN AUTO', 235, 221)
textEl70.color(Color(panelMateColorTo24Bit(7)))
textEl70.size(12)
textEl70.visible(plcReference['%M0033'])

#Visual Order 72
rectangleEl72 = Rectangle(screen, 316, 120, 104-1, 135-1)
rectangleEl72.color(Color(panelMateColorTo24Bit(18))) 
rectangleEl72.border(Color(panelMateColorTo24Bit(7)))
rectangleEl72.border_width(1)

#Visual Order 73 (Visibility Conditional)
textEl73 = Text(screen, 'DRIVE NOT',  332, 206)
textEl73.color(Color(panelMateColorTo24Bit(7)))
textEl73.size(12)
textEl73.visible(plcReference['%M0034'])

#Visual Order 74
rectangleEl74 = Rectangle(screen, 328, 156,  78-1,  32-1)
rectangleEl74.color(Color(panelMateColorTo24Bit( 8))) 
rectangleEl74.border(Color(panelMateColorTo24Bit(17)))
rectangleEl74.border_width(2)

#Visual Order 75
textEl75 = Text(screen, 'YPM', 376, 166)
textEl75.color(Color(panelMateColorTo24Bit(2)))
textEl75.size(12)

#Visual Order 76
readOutEl76 = Text(screen, plcReference['%R0104'], 337, 165)
readOutEl76.color(Color(panelMateColorTo24Bit(2)))
readOutEl76.size(10)

#Visual Order 77
lineEl77 = Line(screen, 331, 157, 403, 157)                         
lineEl77.thickness(2)                                   
lineEl77.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 78
lineEl78 = Line(screen, 329, 186, 329, 157)                         
lineEl78.thickness(2)                                   
lineEl78.color(Color(panelMateColorTo24Bit(7)))         

#Visual Order 79
textEl79 = Text(screen, 'PULL ROLL', 332, 124)
textEl79.color(Color(panelMateColorTo24Bit(0)))
textEl79.size(12)

#Visual Order 80 (Visibility Conditional)
textEl80 = Text(screen, 'IN AUTO', 340, 221)
textEl80.color(Color(panelMateColorTo24Bit(7)))
textEl80.size(12)
textEl80.visible(plcReference['%M0034'])

#Visual Order 82 (Normally On Momentary: [%M0233])                    
conButtonEl82 = Rectangle(screen,   0, 369, 85, 41)
conButtonEl82.color(Color(panelMateColorTo24Bit(18)))
conButtonEl82.border(Color(panelMateColorTo24Bit(0)))
conButtonEl82.border_width(1)
conButtonEl82.back()

#Visual Order 83
textEl83 = Text(screen, 'DRIVE',  23, 373)
textEl83.color(Color(panelMateColorTo24Bit(0)))
textEl83.size(12)

#Visual Order 84
textEl83 = Text(screen, 'FLT RESET',   7, 388)
textEl83.color(Color(panelMateColorTo24Bit(0)))
textEl83.size(12)

#Visual Order 85 (Normally On Momentary: [%M0260])                    
conButtonEl85 = Rectangle(screen, 214, 369, 75, 48)
conButtonEl85.color(Color(panelMateColorTo24Bit(18)))
conButtonEl85.border(Color(panelMateColorTo24Bit(0)))
conButtonEl85.border_width(1)
conButtonEl85.back()

#Visual Order 86
textEl86 = Text(screen, 'MASTER', 227, 375)
textEl86.color(Color(panelMateColorTo24Bit(18)))
textEl86.size(12)

#Visual Order 87
textEl87 = Text(screen, 'RESET', 231, 390)
textEl87.color(Color(panelMateColorTo24Bit(18)))
textEl87.size(12)

#Visual Order 89 (Normally On Momentary: [%M0800])                    
conButtonEl89 = Rectangle(screen,   5, 277, 45, 48)
conButtonEl89.color(Color(panelMateColorTo24Bit(18)))
conButtonEl89.border(Color(panelMateColorTo24Bit(0)))
conButtonEl89.border_width(1)
conButtonEl89.back()

#Visual Order 90
lineEl90 = Line(screen,  26, 285,  26, 319)                         
lineEl90.thickness(3)                                   
lineEl90.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 91
lineEl91 = Line(screen,  26, 285,  34, 297)                         
lineEl91.thickness(3)                                   
lineEl91.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 92
lineEl92 = Line(screen,  18, 296,  25, 285)                         
lineEl92.thickness(3)                                   
lineEl92.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 93
textEl93 = Text(screen, 'Speed Ratio',   5, 257)
textEl93.color(Color(panelMateColorTo24Bit(7)))
textEl93.size(12)

#Visual Order 94 (Normally On Momentary: [%M0801])                    
conButtonEl94 = Rectangle(screen,  55, 277, 42, 48)
conButtonEl94.color(Color(panelMateColorTo24Bit(18)))
conButtonEl94.border(Color(panelMateColorTo24Bit(0)))
conButtonEl94.border_width(1)
conButtonEl94.back()

#Visual Order 95
lineEl95 = Line(screen,  75, 283,  75, 317)                         
lineEl95.thickness(3)                                   
lineEl95.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 96
lineEl96 = Line(screen,  65, 304,  73, 316)                         
lineEl96.thickness(3)                                   
lineEl96.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 97
lineEl97 = Line(screen,  77, 316,  84, 305)                         
lineEl97.thickness(3)                                   
lineEl97.color(Color(panelMateColorTo24Bit(0)))         

#Visual Order 98 (Normally On Momentary: [%M0802])                    
conButtonEl98 = Rectangle(screen, 112, 277, 45, 48)
conButtonEl98.color(Color(panelMateColorTo24Bit(18)))
conButtonEl98.border(Color(panelMateColorTo24Bit(0)))
conButtonEl98.border_width(1)
conButtonEl98.back()

#Visual Order 99
lineEl99 = Line(screen, 135, 284, 135, 318)                         
lineEl99.thickness(3)                                   
lineEl99.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 100
lineEl100 = Line(screen, 135, 284, 143, 296)                         
lineEl100.thickness(3)                                   
lineEl100.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 101
lineEl101 = Line(screen, 127, 295, 134, 284)                         
lineEl101.thickness(3)                                   
lineEl101.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 102
textEl102 = Text(screen, 'Speed Ratio', 116, 257)
textEl102.color(Color(panelMateColorTo24Bit(7)))
textEl102.size(12)

#Visual Order 103 (Normally On Momentary: [%M0803])                    
conButtonEl103 = Rectangle(screen, 164, 277, 42, 48)
conButtonEl103.color(Color(panelMateColorTo24Bit(18)))
conButtonEl103.border(Color(panelMateColorTo24Bit(0)))
conButtonEl103.border_width(1)
conButtonEl103.back()

#Visual Order 104
lineEl104 = Line(screen, 184, 282, 184, 316)                         
lineEl104.thickness(3)                                   
lineEl104.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 105
lineEl105 = Line(screen, 174, 303, 182, 315)                         
lineEl105.thickness(3)                                   
lineEl105.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 106 (Normally On Momentary: [%M0804])                    
conButtonEl106 = Rectangle(screen, 219, 277, 45, 48)
conButtonEl106.color(Color(panelMateColorTo24Bit(18)))
conButtonEl106.border(Color(panelMateColorTo24Bit(0)))
conButtonEl106.border_width(1)
conButtonEl106.back()

#Visual Order 107
lineEl107 = Line(screen, 241, 283, 241, 317)                         
lineEl107.thickness(3)                                   
lineEl107.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 108
lineEl108 = Line(screen, 241, 282, 249, 294)                         
lineEl108.thickness(3)                                   
lineEl108.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 109
lineEl109 = Line(screen, 233, 293, 240, 282)                         
lineEl109.thickness(3)                                   
lineEl109.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 110
textEl110 = Text(screen, 'Speed Ratio', 221, 257)
textEl110.color(Color(panelMateColorTo24Bit(7)))
textEl110.size(12)

#Visual Order 111 (Normally On Momentary: [%M0805])                    
conButtonEl111 = Rectangle(screen, 270, 277, 42, 48)
conButtonEl111.color(Color(panelMateColorTo24Bit(18)))
conButtonEl111.border(Color(panelMateColorTo24Bit(0)))
conButtonEl111.border_width(1)
conButtonEl111.back()

#Visual Order 112
lineEl112 = Line(screen, 290, 283, 290, 317)                         
lineEl112.thickness(3)                                   
lineEl112.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 113
lineEl113 = Line(screen, 280, 303, 288, 315)                         
lineEl113.thickness(3)                                   
lineEl113.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 114
lineEl114 = Line(screen, 292, 315, 299, 304)                         
lineEl114.thickness(3)                                   
lineEl114.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 115 (Normally On Momentary: [%M0806)                    
conButtonEl115 = Rectangle(screen, 325, 277, 45, 48)
conButtonEl115.color(Color(panelMateColorTo24Bit(18)))
conButtonEl115.border(Color(panelMateColorTo24Bit(0)))
conButtonEl115.border_width(1)
conButtonEl115.back()

#Visual Order 116
lineEl116 = Line(screen, 347, 286, 347, 320)                         
lineEl116.thickness(3)                                   
lineEl116.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 117
lineEl117 = Line(screen, 348, 283, 356, 295)                         
lineEl117.thickness(3)                                   
lineEl117.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 118
lineEl118 = Line(screen, 340, 294, 347, 283)                         
lineEl118.thickness(3)                                   
lineEl118.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 119
textEl119 = Text(screen, 'Speed Ratio', 325, 257)
textEl119.color(Color(panelMateColorTo24Bit(7)))
textEl119.size(12)

#Visual Order 120 (Normally On Momentary: [%M0807])                    
conButtonEl120 = Rectangle(screen, 376, 277, 42, 48)
conButtonEl120.color(Color(panelMateColorTo24Bit(18)))
conButtonEl120.border(Color(panelMateColorTo24Bit(0)))
conButtonEl120.border_width(1)
conButtonEl120.back()

#Visual Order 121
lineEl121 = Line(screen, 396, 283, 396, 317)                         
lineEl121.thickness(3)                                   
lineEl121.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 122
lineEl122 = Line(screen, 387, 304, 395, 316)                         
lineEl122.thickness(3)                                   
lineEl122.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 123
lineEl123 = Line(screen, 397, 316, 404, 305)                         
lineEl123.thickness(3)                                   
lineEl123.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 124 (Normally On Momentary: [%M0808])                    
conButtonEl124 = Rectangle(screen, 430, 277, 42, 48)
conButtonEl124.color(Color(panelMateColorTo24Bit(18)))
conButtonEl124.border(Color(panelMateColorTo24Bit(0)))
conButtonEl124.border_width(1)
conButtonEl124.back()

#Visual Order 125
lineEl125 = Line(screen, 453, 280, 453, 314)                         
lineEl125.thickness(3)                                   
lineEl125.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 126
lineEl126 = Line(screen, 453, 280, 461, 292)                         
lineEl126.thickness(3)                                   
lineEl126.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 127
lineEl127 = Line(screen, 445, 291, 452, 280)                         
lineEl127.thickness(3)                                   
lineEl127.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 128
textEl128 = Text(screen, 'Speed Ratio', 430, 257)
textEl128.color(Color(panelMateColorTo24Bit(7)))
textEl128.size(12)

#Visual Order 129 (Normally On Momentary: [%M0809])                    
conButtonEl129 = Rectangle(screen, 480, 277, 42, 48)
conButtonEl129.color(Color(panelMateColorTo24Bit(18)))
conButtonEl129.border(Color(panelMateColorTo24Bit(0)))
conButtonEl129.border_width(1)
conButtonEl129.back()

#Visual Order 130
lineEl130 = Line(screen, 501, 282, 501, 316)                         
lineEl130.thickness(3)                                   
lineEl130.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 131
lineEl131 = Line(screen, 492, 301, 500, 313)                         
lineEl131.thickness(3)                                   
lineEl131.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 132
lineEl132 = Line(screen, 503, 313, 510, 302)                         
lineEl132.thickness(3)                                   
lineEl132.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 133
lineEl133 = Line(screen, 210, 255, 210, 325)                         
lineEl133.thickness(1)                                   
lineEl133.color(Color(panelMateColorTo24Bit(7)))

#Visual Order 134
lineEl134 = Line(screen, 420, 255, 420, 325)                         
lineEl134.thickness(1)                                   
lineEl134.color(Color(panelMateColorTo24Bit(7)))

#Visual Order 135
lineEl135 = Line(screen, 315, 255, 315, 325)                         
lineEl135.thickness(1)                                   
lineEl135.color(Color(panelMateColorTo24Bit(7)))

#Visual Order 136
lineEl136 = Line(screen, 106, 255, 106, 325)                         
lineEl136.thickness(1)                                   
lineEl136.color(Color(panelMateColorTo24Bit(7)))

#Visual Order 137
lineEl137 = Line(screen,   2, 325, 526, 325)                         
lineEl137.thickness(1)                                   
lineEl137.color(Color(panelMateColorTo24Bit(7)))

#Visual Order 138
textEl138 = Text(screen, 'INC',  14, 307)
textEl138.color(Color(panelMateColorTo24Bit(00)))
textEl138.size(12)

#Visual Order 139
textEl139 = Text(screen, 'DEC',  63, 282)
textEl139.color(Color(panelMateColorTo24Bit(00)))
textEl139.size(12)

#Visual Order 140
textEl140 = Text(screen, 'INC', 123, 304)
textEl140.color(Color(panelMateColorTo24Bit(00)))
textEl140.size(12)

#Visual Order 141
textEl141 = Text(screen, 'INC', 229, 304)
textEl141.color(Color(panelMateColorTo24Bit(00)))
textEl141.size(12)

#Visual Order 142
textEl142 = Text(screen, 'INC', 335, 304)
textEl142.color(Color(panelMateColorTo24Bit(00)))
textEl142.size(12)

#Visual Order 143
textEl143 = Text(screen, 'INC', 443, 304)
textEl143.color(Color(panelMateColorTo24Bit(00)))
textEl143.size(12)

#Visual Order 144
textEl144 = Text(screen, 'DEC', 172, 282)
textEl144.color(Color(panelMateColorTo24Bit(00)))
textEl144.size(12)

#Visual Order 145
textEl145 = Text(screen, 'DEC', 279, 282)
textEl145.color(Color(panelMateColorTo24Bit(00)))
textEl145.size(12)

#Visual Order 146
textEl146 = Text(screen, 'DEC', 384, 282)
textEl146.color(Color(panelMateColorTo24Bit(00)))
textEl146.size(12)

#Visual Order 147
textEl147 = Text(screen, 'DEC', 490, 282)
textEl147.color(Color(panelMateColorTo24Bit(00)))
textEl147.size(12)

#Visual Order 148
lineEl148 = Line(screen, 185, 315, 192, 304)                         
lineEl148.thickness(3)                                   
lineEl148.color(Color(panelMateColorTo24Bit(0)))

#Visual Order 149 (Toggle [%M0810])                    
conButtonEl149 = Rectangle(screen,   6, 333, 89, 28)
conButtonEl149.color(Color(panelMateColorTo24Bit(18)))
conButtonEl149.border(Color(panelMateColorTo24Bit(0)))
conButtonEl149.border_width(1)
conButtonEl149.back()
conButtonEl149.visible(not plcReference['%Q0056'])

#Visual Order 150 (Conditional)
textEl150 = Text(screen, 'FORWARD', 22, 339)
textEl150.color(Color(panelMateColorTo24Bit(0)))
textEl150.size(12)
textEl150.visible(not plcReference['%M0810'])

#Visual Order 151 (Conditional)
textEl151 = Text(screen, 'REVERSE', 22, 339)
textEl151.color(Color(panelMateColorTo24Bit(0)))
textEl151.size(12)
textEl151.visible(plcReference['%M0810'])

#Visual Order 152 (Toggle [%M0811])                    
conButtonEl152 = Rectangle(screen, 114, 333, 89, 28)
conButtonEl152.color(Color(panelMateColorTo24Bit(18)))
conButtonEl152.border(Color(panelMateColorTo24Bit(0)))
conButtonEl152.border_width(1)
conButtonEl152.back()
conButtonEl152.visible(not plcReference['%Q0056'])

#Visual Order 153 (Conditional)
textEl153 = Text(screen, 'FORWARD', 130, 339)
textEl153.color(Color(panelMateColorTo24Bit(0)))
textEl153.size(12)
textEl153.visible(not plcReference['%M0811'])

#Visual Order 154 (Conditional)
textEl154 = Text(screen, 'REVERSE', 130, 339)
textEl154.color(Color(panelMateColorTo24Bit(0)))
textEl154.size(12)
textEl154.visible(plcReference['%M0811'])

#Visual Order 155 (Toggle [%M0812])                    
conButtonEl155 = Rectangle(screen, 220, 333, 89, 28)
conButtonEl155.color(Color(panelMateColorTo24Bit(18)))
conButtonEl155.border(Color(panelMateColorTo24Bit(0)))
conButtonEl155.border_width(1)
conButtonEl155.back()
conButtonEl155.visible(not plcReference['%Q0056'])

#Visual Order 156 (Conditional)
textEl156 = Text(screen, 'FORWARD', 236, 339)
textEl156.color(Color(panelMateColorTo24Bit(0)))
textEl156.size(12)
textEl156.visible(not plcReference['%M0812'])

#Visual Order 157 (Conditional)
textEl157 = Text(screen, 'REVERSE', 236, 339)
textEl157.color(Color(panelMateColorTo24Bit(0)))
textEl157.size(12)
textEl157.visible(plcReference['%M0812'])

##########
# Render #
##########
fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)
    if (screen.size() == (-1, -1)): # exit when screen closes
        break