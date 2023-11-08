from pydraw import *

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

screen = Screen(640, 480, 'Page: Drives 4')
screen.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 2
text_element_2 = Text(screen, "EXIT", 470, 437)
text_element_2.color(Color(panelMateColorTo24Bit(0)))
text_element_2.size(12)

# Visual Order 4
text_element_4 = Text(screen, "PAGE UP", 456, 388)
text_element_4.color(Color(panelMateColorTo24Bit(0)))
text_element_4.size(12)

# Visual Order 6
text_element_6 = Text(screen, "DRIVE", 466, 330)
text_element_6.color(Color(panelMateColorTo24Bit(0)))
text_element_6.size(12)

# Visual Order 7
text_element_7 = Text(screen, "FLT RESET", 450, 345)
text_element_7.color(Color(panelMateColorTo24Bit(0)))
text_element_7.size(12)

# Visual Order 8
rectangle_element_8 = Rectangle(screen, 6, 112, 103 - 1 , 352 - 1 )
rectangle_element_8.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_8.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_8.border_width(1)

# Visual Order 9
line_element_9 = Line(screen, 109, 229, 109, 410)
line_element_9.thickness(1)
line_element_9.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 10
line_element_10 = Line(screen, 108, 459, 108, 226)
line_element_10.thickness(3)
line_element_10.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 11
line_element_11 = Line(screen, 6, 113, 66, 113)
line_element_11.thickness(1)
line_element_11.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 12
line_element_12 = Line(screen, 6, 114, 65, 114)
line_element_12.thickness(1)
line_element_12.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 13
line_element_13 = Line(screen, 8, 115, 63, 115)
line_element_13.thickness(1)
line_element_13.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 14
line_element_14 = Line(screen, 6, 462, 66, 462)
line_element_14.thickness(3)
line_element_14.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 15
line_element_15 = Line(screen, 6, 225, 6, 459)
line_element_15.thickness(3)
line_element_15.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 16
line_element_16 = Line(screen, 5, 461, 22, 461)
line_element_16.thickness(1)
line_element_16.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 17
line_element_17 = Line(screen, 6, 461, 23, 461)
line_element_17.thickness(1)
line_element_17.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 18
text_element_18 = Text(screen, "BELT", 43, 137)
text_element_18.color(Color(panelMateColorTo24Bit(0)))
text_element_18.size(12)

# Visual Order 19
line_element_19 = Line(screen, 49, 113, 109, 113)
line_element_19.thickness(1)
line_element_19.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 20
line_element_20 = Line(screen, 49, 114, 108, 114)
line_element_20.thickness(1)
line_element_20.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 21
line_element_21 = Line(screen, 51, 115, 106, 115)
line_element_21.thickness(1)
line_element_21.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 22
line_element_22 = Line(screen, 48, 462, 108, 462)
line_element_22.thickness(3)
line_element_22.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 23
line_element_23 = Line(screen, 109, 119, 109, 300)
line_element_23.thickness(1)
line_element_23.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 24
line_element_24 = Line(screen, 108, 116, 108, 298)
line_element_24.thickness(3)
line_element_24.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 25
line_element_25 = Line(screen, 6, 114, 6, 300)
line_element_25.thickness(3)
line_element_25.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 26
rectangle_element_26 = Rectangle(screen, 9, 120, 95 - 1 , 51 - 1 )
rectangle_element_26.color(Color(panelMateColorTo24Bit(255)))
rectangle_element_26.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_26.border_width(1)

# Visual Order 27
line_element_27 = Line(screen, 103, 120, 103, 170)
line_element_27.thickness(1)
line_element_27.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 28
rectangle_element_28 = Rectangle(screen, 18, 235, 78 - 1 , 32 - 1 )
rectangle_element_28.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_28.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_28.border_width(2)

# Visual Order 29
text_element_29 = Text(screen, "SETPOINT", 27, 219)
text_element_29.color(Color(panelMateColorTo24Bit(0)))
text_element_29.size(12)

# Visual Order 30
text_element_30 = Text(screen, "%", 70, 245)
text_element_30.color(Color(panelMateColorTo24Bit(6)))
text_element_30.size(12)

# Visual Order 32
line_element_32 = Line(screen, 21, 236, 93, 236)
line_element_32.thickness(2)
line_element_32.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 33
line_element_33 = Line(screen, 20, 236, 20, 265)
line_element_33.thickness(2)
line_element_33.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 34
line_element_34 = Line(screen, 74, 235, 92, 235)
line_element_34.thickness(1)
line_element_34.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 35
rectangle_element_35 = Rectangle(screen, 21, 285, 74 - 1 , 37 - 1 )
rectangle_element_35.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_35.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_35.border_width(1)

# Visual Order 36
line_element_36 = Line(screen, 93, 321, 93, 285)
line_element_36.thickness(1)
line_element_36.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 37
line_element_37 = Line(screen, 92, 321, 92, 285)
line_element_37.thickness(1)
line_element_37.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 38
line_element_38 = Line(screen, 22, 285, 93, 285)
line_element_38.thickness(1)
line_element_38.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 39
line_element_39 = Line(screen, 24, 286, 92, 286)
line_element_39.thickness(1)
line_element_39.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 40
line_element_40 = Line(screen, 25, 287, 91, 287)
line_element_40.thickness(1)
line_element_40.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 41
line_element_41 = Line(screen, 21, 320, 21, 285)
line_element_41.thickness(1)
line_element_41.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 42
line_element_42 = Line(screen, 22, 320, 22, 285)
line_element_42.thickness(1)
line_element_42.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 43
line_element_43 = Line(screen, 23, 320, 23, 285)
line_element_43.thickness(1)
line_element_43.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 44
line_element_44 = Line(screen, 21, 285, 24, 287)
line_element_44.thickness(1)
line_element_44.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 45
line_element_45 = Line(screen, 21, 321, 94, 321)
line_element_45.thickness(1)
line_element_45.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 46
line_element_46 = Line(screen, 25, 320, 94, 320)
line_element_46.thickness(1)
line_element_46.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 47
line_element_47 = Line(screen, 26, 319, 92, 319)
line_element_47.thickness(1)
line_element_47.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 48
line_element_48 = Line(screen, 91, 318, 93, 321)
line_element_48.thickness(1)
line_element_48.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 49
rectangle_element_49 = Rectangle(screen, 20, 284, 75 - 1 , 39 - 1 )
rectangle_element_49.color(Color(panelMateColorTo24Bit(255)))
rectangle_element_49.border(Color(panelMateColorTo24Bit(0)))
rectangle_element_49.border_width(1)

# Visual Order 51
line_element_51 = Line(screen, 35, 287, 84, 287)
line_element_51.thickness(1)
line_element_51.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 52
line_element_52 = Line(screen, 35, 285, 86, 285)
line_element_52.thickness(1)
line_element_52.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 53
line_element_53 = Line(screen, 33, 286, 81, 286)
line_element_53.thickness(1)
line_element_53.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 54
text_element_54 = Text(screen, "KEYPAD", 35, 268)
text_element_54.color(Color(panelMateColorTo24Bit(0)))
text_element_54.size(12)

# Visual Order 56
text_element_56 = Text(screen, "OVERFEED", 26, 152)
text_element_56.color(Color(panelMateColorTo24Bit(0)))
text_element_56.size(12)

# Visual Order 58
text_element_58 = Text(screen, "OVEN", 43, 122)
text_element_58.color(Color(panelMateColorTo24Bit(0)))
text_element_58.size(12)

# Visual Order 59
rectangle_element_59 = Rectangle(screen, 17, 187, 78 - 1 , 32 - 1 )
rectangle_element_59.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_59.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_59.border_width(2)

# Visual Order 60
line_element_60 = Line(screen, 9, 170, 101, 170)
line_element_60.thickness(1)
line_element_60.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 61
text_element_61 = Text(screen, "ACTUAL", 34, 172)
text_element_61.color(Color(panelMateColorTo24Bit(0)))
text_element_61.size(12)

# Visual Order 62
text_element_62 = Text(screen, "%", 71, 197)
text_element_62.color(Color(panelMateColorTo24Bit(2)))
text_element_62.size(12)

# Visual Order 64
line_element_64 = Line(screen, 20, 188, 92, 188)
line_element_64.thickness(2)
line_element_64.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 65
line_element_65 = Line(screen, 19, 188, 19, 217)
line_element_65.thickness(2)
line_element_65.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 66
line_element_66 = Line(screen, 73, 187, 91, 187)
line_element_66.thickness(1)
line_element_66.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 67
rectangle_element_67 = Rectangle(screen, 116, 112, 103 - 1 , 352 - 1 )
rectangle_element_67.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_67.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_67.border_width(1)

# Visual Order 68
line_element_68 = Line(screen, 219, 229, 219, 410)
line_element_68.thickness(1)
line_element_68.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 69
line_element_69 = Line(screen, 218, 459, 218, 226)
line_element_69.thickness(3)
line_element_69.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 70
line_element_70 = Line(screen, 116, 113, 176, 113)
line_element_70.thickness(1)
line_element_70.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 71
line_element_71 = Line(screen, 116, 114, 175, 114)
line_element_71.thickness(1)
line_element_71.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 72
line_element_72 = Line(screen, 118, 115, 173, 115)
line_element_72.thickness(1)
line_element_72.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 73
line_element_73 = Line(screen, 116, 462, 176, 462)
line_element_73.thickness(3)
line_element_73.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 74
line_element_74 = Line(screen, 116, 225, 116, 459)
line_element_74.thickness(3)
line_element_74.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 75
line_element_75 = Line(screen, 115, 461, 132, 461)
line_element_75.thickness(1)
line_element_75.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 76
line_element_76 = Line(screen, 116, 461, 133, 461)
line_element_76.thickness(1)
line_element_76.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 77
text_element_77 = Text(screen, "SECTION", 139, 137)
text_element_77.color(Color(panelMateColorTo24Bit(0)))
text_element_77.size(12)

# Visual Order 78
line_element_78 = Line(screen, 159, 113, 219, 113)
line_element_78.thickness(1)
line_element_78.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 79
line_element_79 = Line(screen, 159, 114, 218, 114)
line_element_79.thickness(1)
line_element_79.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 80
line_element_80 = Line(screen, 161, 115, 216, 115)
line_element_80.thickness(1)
line_element_80.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 81
line_element_81 = Line(screen, 158, 462, 218, 462)
line_element_81.thickness(3)
line_element_81.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 82
line_element_82 = Line(screen, 219, 119, 219, 300)
line_element_82.thickness(1)
line_element_82.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 83
line_element_83 = Line(screen, 218, 116, 218, 298)
line_element_83.thickness(3)
line_element_83.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 84
line_element_84 = Line(screen, 116, 114, 116, 300)
line_element_84.thickness(3)
line_element_84.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 85
rectangle_element_85 = Rectangle(screen, 119, 120, 95 - 1 , 51 - 1 )
rectangle_element_85.color(Color(panelMateColorTo24Bit(255)))
rectangle_element_85.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_85.border_width(1)

# Visual Order 86
line_element_86 = Line(screen, 213, 120, 213, 170)
line_element_86.thickness(1)
line_element_86.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 87
rectangle_element_87 = Rectangle(screen, 128, 235, 78 - 1 , 32 - 1 )
rectangle_element_87.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_87.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_87.border_width(2)

# Visual Order 88
text_element_88 = Text(screen, "SETPOINT", 137, 219)
text_element_88.color(Color(panelMateColorTo24Bit(0)))
text_element_88.size(12)

# Visual Order 89
text_element_89 = Text(screen, "%", 180, 245)
text_element_89.color(Color(panelMateColorTo24Bit(6)))
text_element_89.size(12)

# Visual Order 91
line_element_91 = Line(screen, 131, 236, 203, 236)
line_element_91.thickness(2)
line_element_91.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 92
line_element_92 = Line(screen, 130, 236, 130, 265)
line_element_92.thickness(2)
line_element_92.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 93
line_element_93 = Line(screen, 184, 235, 202, 235)
line_element_93.thickness(1)
line_element_93.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 94
rectangle_element_94 = Rectangle(screen, 131, 285, 74 - 1 , 37 - 1 )
rectangle_element_94.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_94.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_94.border_width(1)

# Visual Order 95
line_element_95 = Line(screen, 203, 321, 203, 285)
line_element_95.thickness(1)
line_element_95.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 96
line_element_96 = Line(screen, 202, 321, 202, 285)
line_element_96.thickness(1)
line_element_96.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 97
line_element_97 = Line(screen, 132, 285, 203, 285)
line_element_97.thickness(1)
line_element_97.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 98
line_element_98 = Line(screen, 134, 286, 202, 286)
line_element_98.thickness(1)
line_element_98.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 99
line_element_99 = Line(screen, 135, 287, 201, 287)
line_element_99.thickness(1)
line_element_99.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 100
line_element_100 = Line(screen, 131, 320, 131, 285)
line_element_100.thickness(1)
line_element_100.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 101
line_element_101 = Line(screen, 132, 320, 132, 285)
line_element_101.thickness(1)
line_element_101.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 102
line_element_102 = Line(screen, 133, 320, 133, 285)
line_element_102.thickness(1)
line_element_102.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 103
line_element_103 = Line(screen, 131, 285, 134, 287)
line_element_103.thickness(1)
line_element_103.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 104
line_element_104 = Line(screen, 131, 321, 204, 321)
line_element_104.thickness(1)
line_element_104.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 105
line_element_105 = Line(screen, 135, 320, 204, 320)
line_element_105.thickness(1)
line_element_105.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 106
line_element_106 = Line(screen, 136, 319, 202, 319)
line_element_106.thickness(1)
line_element_106.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 107
line_element_107 = Line(screen, 201, 318, 203, 321)
line_element_107.thickness(1)
line_element_107.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 108
rectangle_element_108 = Rectangle(screen, 130, 284, 75 - 1 , 39 - 1 )
rectangle_element_108.color(Color(panelMateColorTo24Bit(255)))
rectangle_element_108.border(Color(panelMateColorTo24Bit(0)))
rectangle_element_108.border_width(1)

# Visual Order 110
line_element_110 = Line(screen, 145, 287, 194, 287)
line_element_110.thickness(1)
line_element_110.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 111
line_element_111 = Line(screen, 145, 285, 196, 285)
line_element_111.thickness(1)
line_element_111.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 112
line_element_112 = Line(screen, 143, 286, 191, 286)
line_element_112.thickness(1)
line_element_112.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 113
text_element_113 = Text(screen, "KEYPAD", 145, 268)
text_element_113.color(Color(panelMateColorTo24Bit(0)))
text_element_113.size(12)

# Visual Order 114
text_element_114 = Text(screen, "OVERFEED", 135, 152)
text_element_114.color(Color(panelMateColorTo24Bit(0)))
text_element_114.size(12)

# Visual Order 115
text_element_115 = Text(screen, "ENTRY", 147, 122)
text_element_115.color(Color(panelMateColorTo24Bit(0)))
text_element_115.size(12)

# Visual Order 116
rectangle_element_116 = Rectangle(screen, 127, 187, 78 - 1 , 32 - 1 )
rectangle_element_116.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_116.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_116.border_width(2)

# Visual Order 117
line_element_117 = Line(screen, 119, 170, 211, 170)
line_element_117.thickness(1)
line_element_117.color(Color(panelMateColorTo24Bit(17)))

# Visual Order 118
text_element_118 = Text(screen, "ACTUAL", 144, 172)
text_element_118.color(Color(panelMateColorTo24Bit(0)))
text_element_118.size(12)

# Visual Order 119
text_element_119 = Text(screen, "%", 181, 197)
text_element_119.color(Color(panelMateColorTo24Bit(2)))
text_element_119.size(12)

# Visual Order 121
line_element_121 = Line(screen, 130, 188, 202, 188)
line_element_121.thickness(2)
line_element_121.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 122
line_element_122 = Line(screen, 129, 188, 129, 217)
line_element_122.thickness(2)
line_element_122.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 123
line_element_123 = Line(screen, 183, 187, 201, 187)
line_element_123.thickness(1)
line_element_123.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 125
text_element_125 = Text(screen, "ALARM", 466, 277)
text_element_125.color(Color(panelMateColorTo24Bit(0)))
text_element_125.size(12)

# Visual Order 126
text_element_126 = Text(screen, "RESET", 467, 291)
text_element_126.color(Color(panelMateColorTo24Bit(0)))
text_element_126.size(12)

fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)
    if (screen.size() == (-1, -1)): # exit when screen closes
        break
