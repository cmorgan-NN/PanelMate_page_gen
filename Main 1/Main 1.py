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

screen = Screen(640, 480, 'Page: Main 1')
screen.color(Color(panelMateColorTo24Bit(0)))

plc_references = {

    #Internal Coils (%M in GE Fanuc PLC)
    '%M0031' : False,
    '%M0035' : False,
    '%M0032' : False,
    '%M0033' : False,
    '%M0034' : False,
    '%M0810' : False,
    '%M0811' : False,
    '%M0812' : False

}

# Visual Order 1
rectangle_element_1 = Rectangle(screen, 1, 120, 104 - 1 , 135 - 1 )
rectangle_element_1.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_1.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_1.border_width(1)

# Visual Order 2
text_element_2 = Text(screen, "DRIVE NOT", 17, 205)
text_element_2.color(Color(panelMateColorTo24Bit(7)))
text_element_2.size(12)
text_element_2.visible(plc_references['%M0031'])

# Visual Order 3
text_element_3 = Text(screen, "ENABLED", 25, 221)
text_element_3.color(Color(panelMateColorTo24Bit(7)))
text_element_3.size(12)
text_element_3.visible(plc_references['%M0031'])

# Visual Order 5
text_element_5 = Text(screen, "NEXT", 470, 374)
text_element_5.color(Color(panelMateColorTo24Bit(0)))
text_element_5.size(12)

# Visual Order 6
text_element_6 = Text(screen, "PAGE", 470, 392)
text_element_6.color(Color(panelMateColorTo24Bit(0)))
text_element_6.size(12)

# Visual Order 7
text_element_7 = Text(screen, "LINE", 132, 388)
text_element_7.color(Color(panelMateColorTo24Bit(3)))
text_element_7.size(12)

# Visual Order 8
text_element_8 = Text(screen, "SPEED", 129, 403)
text_element_8.color(Color(panelMateColorTo24Bit(3)))
text_element_8.size(12)

# Visual Order 9
rectangle_element_9 = Rectangle(screen, 108, 422, 78 - 1 , 32 - 1 )
rectangle_element_9.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_9.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_9.border_width(2)

# Visual Order 10
text_element_10 = Text(screen, "YPM", 156, 431)
text_element_10.color(Color(panelMateColorTo24Bit(2)))
text_element_10.size(12)

# Visual Order 12
line_element_12 = Line(screen, 111, 423, 183, 423)
line_element_12.thickness(2)
line_element_12.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 13
line_element_13 = Line(screen, 110, 423, 110, 452)
line_element_13.thickness(2)
line_element_13.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 14
line_element_14 = Line(screen, 164, 422, 182, 422)
line_element_14.thickness(1)
line_element_14.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 15
rectangle_element_15 = Rectangle(screen, 102, 382, 90 - 1 , 80 - 1 )
rectangle_element_15.color(Color(panelMateColorTo24Bit(255)))
rectangle_element_15.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_15.border_width(1)

# Visual Order 20
text_element_20 = Text(screen, "EXHAUST", 225, 421)
text_element_20.color(Color(panelMateColorTo24Bit(0)))
text_element_20.size(12)

# Visual Order 21
text_element_21 = Text(screen, "CIRC.", 307, 420)
text_element_21.color(Color(panelMateColorTo24Bit(0)))
text_element_21.size(12)

# Visual Order 22
text_element_22 = Text(screen, "FANS", 309, 439)
text_element_22.color(Color(panelMateColorTo24Bit(0)))
text_element_22.size(12)

# Visual Order 23
text_element_23 = Text(screen, "FAN", 237, 438)
text_element_23.color(Color(panelMateColorTo24Bit(0)))
text_element_23.size(12)

# Visual Order 24
text_element_24 = Text(screen, "BURNER", 375, 421)
text_element_24.color(Color(panelMateColorTo24Bit(0)))
text_element_24.size(12)

# Visual Order 25
text_element_25 = Text(screen, "CONTROL", 373, 438)
text_element_25.color(Color(panelMateColorTo24Bit(0)))
text_element_25.size(12)

# Visual Order 27
text_element_27 = Text(screen, "LINE", 469, 421)
text_element_27.color(Color(panelMateColorTo24Bit(0)))
text_element_27.size(12)

# Visual Order 28
text_element_28 = Text(screen, "SPEED", 466, 439)
text_element_28.color(Color(panelMateColorTo24Bit(0)))
text_element_28.size(12)

# Visual Order 29
text_element_29 = Text(screen, "ALARMS", 302, 383)
text_element_29.color(Color(panelMateColorTo24Bit(0)))
text_element_29.size(12)

# Visual Order 31
text_element_31 = Text(screen, "ALARM", 379, 375)
text_element_31.color(Color(panelMateColorTo24Bit(0)))
text_element_31.size(12)

# Visual Order 32
text_element_32 = Text(screen, "RESET", 379, 389)
text_element_32.color(Color(panelMateColorTo24Bit(0)))
text_element_32.size(12)

# Visual Order 33
rectangle_element_33 = Rectangle(screen, 421, 120, 104 - 1 , 135 - 1 )
rectangle_element_33.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_33.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_33.border_width(1)

# Visual Order 34
rectangle_element_34 = Rectangle(screen, 433, 156, 78 - 1 , 32 - 1 )
rectangle_element_34.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_34.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_34.border_width(2)

# Visual Order 35
text_element_35 = Text(screen, "YPM", 481, 166)
text_element_35.color(Color(panelMateColorTo24Bit(2)))
text_element_35.size(12)

# Visual Order 37
line_element_37 = Line(screen, 436, 157, 508, 157)
line_element_37.thickness(2)
line_element_37.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 38
line_element_38 = Line(screen, 434, 186, 434, 157)
line_element_38.thickness(2)
line_element_38.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 39
text_element_39 = Text(screen, "LDER", 444, 124)
text_element_39.color(Color(panelMateColorTo24Bit(High)))
text_element_39.size(12)

# Visual Order 40
rectangle_element_40 = Rectangle(screen, 13, 156, 78 - 1 , 32 - 1 )
rectangle_element_40.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_40.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_40.border_width(2)

# Visual Order 41
text_element_41 = Text(screen, "YPM", 61, 165)
text_element_41.color(Color(panelMateColorTo24Bit(2)))
text_element_41.size(12)

# Visual Order 43
line_element_43 = Line(screen, 16, 157, 88, 157)
line_element_43.thickness(2)
line_element_43.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 44
line_element_44 = Line(screen, 14, 186, 14, 157)
line_element_44.thickness(2)
line_element_44.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 45
text_element_45 = Text(screen, "TRY PAD", 16, 124)
text_element_45.color(Color(panelMateColorTo24Bit(High)))
text_element_45.size(12)

# Visual Order 46
text_element_46 = Text(screen, "IN AUTO", 25, 221)
text_element_46.color(Color(panelMateColorTo24Bit(7)))
text_element_46.size(12)
text_element_46.visible(plc_references['%M0031'])

# Visual Order 47
text_element_47 = Text(screen, "IN AUTO", 445, 221)
text_element_47.color(Color(panelMateColorTo24Bit(7)))
text_element_47.size(12)
text_element_47.visible(plc_references['%M0035'])

# Visual Order 48
text_element_48 = Text(screen, "DRIVE NOT", 437, 206)
text_element_48.color(Color(panelMateColorTo24Bit(7)))
text_element_48.size(12)
text_element_48.visible(plc_references['%M0035'])

# Visual Order 51
rectangle_element_51 = Rectangle(screen, 106, 120, 104 - 1 , 135 - 1 )
rectangle_element_51.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_51.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_51.border_width(1)

# Visual Order 52
text_element_52 = Text(screen, "DRIVE NOT", 122, 206)
text_element_52.color(Color(panelMateColorTo24Bit(7)))
text_element_52.size(12)
text_element_52.visible(plc_references['%M0032'])

# Visual Order 53
rectangle_element_53 = Rectangle(screen, 118, 156, 78 - 1 , 32 - 1 )
rectangle_element_53.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_53.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_53.border_width(2)

# Visual Order 54
text_element_54 = Text(screen, "YPM", 166, 166)
text_element_54.color(Color(panelMateColorTo24Bit(2)))
text_element_54.size(12)

# Visual Order 56
line_element_56 = Line(screen, 121, 157, 193, 157)
line_element_56.thickness(2)
line_element_56.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 57
line_element_57 = Line(screen, 119, 186, 119, 157)
line_element_57.thickness(2)
line_element_57.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 58
line_element_58 = Line(screen, 148, 156, 166, 156)
line_element_58.thickness(1)
line_element_58.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 59
text_element_59 = Text(screen, "EAM ROLLS 1", 106, 124)
text_element_59.color(Color(panelMateColorTo24Bit(High)))
text_element_59.size(12)

# Visual Order 60
text_element_60 = Text(screen, "IN AUTO", 130, 222)
text_element_60.color(Color(panelMateColorTo24Bit(7)))
text_element_60.size(12)
text_element_60.visible(plc_references['%M0032'])

# Visual Order 62
rectangle_element_62 = Rectangle(screen, 211, 120, 104 - 1 , 135 - 1 )
rectangle_element_62.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_62.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_62.border_width(1)

# Visual Order 63
text_element_63 = Text(screen, "DRIVE NOT", 227, 207)
text_element_63.color(Color(panelMateColorTo24Bit(7)))
text_element_63.size(12)
text_element_63.visible(plc_references['%M0033'])

# Visual Order 64
rectangle_element_64 = Rectangle(screen, 223, 156, 78 - 1 , 32 - 1 )
rectangle_element_64.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_64.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_64.border_width(2)

# Visual Order 65
text_element_65 = Text(screen, "YPM", 271, 166)
text_element_65.color(Color(panelMateColorTo24Bit(2)))
text_element_65.size(12)

# Visual Order 67
line_element_67 = Line(screen, 226, 157, 298, 157)
line_element_67.thickness(2)
line_element_67.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 68
line_element_68 = Line(screen, 224, 186, 224, 157)
line_element_68.thickness(2)
line_element_68.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 69
text_element_69 = Text(screen, "EAM ROLLS 2", 211, 124)
text_element_69.color(Color(panelMateColorTo24Bit(High)))
text_element_69.size(12)

# Visual Order 70
text_element_70 = Text(screen, "IN AUTO", 235, 221)
text_element_70.color(Color(panelMateColorTo24Bit(7)))
text_element_70.size(12)
text_element_70.visible(plc_references['%M0033'])

# Visual Order 72
rectangle_element_72 = Rectangle(screen, 316, 120, 104 - 1 , 135 - 1 )
rectangle_element_72.color(Color(panelMateColorTo24Bit(18)))
rectangle_element_72.border(Color(panelMateColorTo24Bit(7)))
rectangle_element_72.border_width(1)

# Visual Order 73
text_element_73 = Text(screen, "DRIVE NOT", 332, 206)
text_element_73.color(Color(panelMateColorTo24Bit(7)))
text_element_73.size(12)
text_element_73.visible(plc_references['%M0034'])

# Visual Order 74
rectangle_element_74 = Rectangle(screen, 328, 156, 78 - 1 , 32 - 1 )
rectangle_element_74.color(Color(panelMateColorTo24Bit(8)))
rectangle_element_74.border(Color(panelMateColorTo24Bit(17)))
rectangle_element_74.border_width(2)

# Visual Order 75
text_element_75 = Text(screen, "YPM", 376, 166)
text_element_75.color(Color(panelMateColorTo24Bit(2)))
text_element_75.size(12)

# Visual Order 77
line_element_77 = Line(screen, 331, 157, 403, 157)
line_element_77.thickness(2)
line_element_77.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 78
line_element_78 = Line(screen, 329, 186, 329, 157)
line_element_78.thickness(2)
line_element_78.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 79
text_element_79 = Text(screen, "LL ROLL", 332, 124)
text_element_79.color(Color(panelMateColorTo24Bit(High)))
text_element_79.size(12)

# Visual Order 80
text_element_80 = Text(screen, "IN AUTO", 340, 221)
text_element_80.color(Color(panelMateColorTo24Bit(7)))
text_element_80.size(12)
text_element_80.visible(plc_references['%M0034'])

# Visual Order 83
text_element_83 = Text(screen, "DRIVE", 23, 373)
text_element_83.color(Color(panelMateColorTo24Bit(0)))
text_element_83.size(12)

# Visual Order 84
text_element_84 = Text(screen, "FLT RESET", 7, 388)
text_element_84.color(Color(panelMateColorTo24Bit(0)))
text_element_84.size(12)

# Visual Order 86
text_element_86 = Text(screen, "MASTER", 227, 375)
text_element_86.color(Color(panelMateColorTo24Bit(0)))
text_element_86.size(12)

# Visual Order 87
text_element_87 = Text(screen, "RESET", 231, 390)
text_element_87.color(Color(panelMateColorTo24Bit(0)))
text_element_87.size(12)

# Visual Order 90
line_element_90 = Line(screen, 26, 285, 26, 319)
line_element_90.thickness(3)
line_element_90.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 91
line_element_91 = Line(screen, 26, 285, 34, 297)
line_element_91.thickness(3)
line_element_91.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 92
line_element_92 = Line(screen, 18, 296, 25, 285)
line_element_92.thickness(3)
line_element_92.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 93
text_element_93 = Text(screen, "Speed Ratio", 5, 257)
text_element_93.color(Color(panelMateColorTo24Bit(7)))
text_element_93.size(12)

# Visual Order 95
line_element_95 = Line(screen, 75, 283, 75, 317)
line_element_95.thickness(3)
line_element_95.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 96
line_element_96 = Line(screen, 65, 304, 73, 316)
line_element_96.thickness(3)
line_element_96.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 97
line_element_97 = Line(screen, 77, 316, 84, 305)
line_element_97.thickness(3)
line_element_97.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 99
line_element_99 = Line(screen, 135, 284, 135, 318)
line_element_99.thickness(3)
line_element_99.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 100
line_element_100 = Line(screen, 135, 284, 143, 296)
line_element_100.thickness(3)
line_element_100.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 101
line_element_101 = Line(screen, 127, 295, 134, 284)
line_element_101.thickness(3)
line_element_101.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 102
text_element_102 = Text(screen, "Speed Ratio", 116, 257)
text_element_102.color(Color(panelMateColorTo24Bit(7)))
text_element_102.size(12)

# Visual Order 104
line_element_104 = Line(screen, 184, 282, 184, 316)
line_element_104.thickness(3)
line_element_104.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 105
line_element_105 = Line(screen, 174, 303, 182, 315)
line_element_105.thickness(3)
line_element_105.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 107
line_element_107 = Line(screen, 241, 283, 241, 317)
line_element_107.thickness(3)
line_element_107.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 108
line_element_108 = Line(screen, 241, 282, 249, 294)
line_element_108.thickness(3)
line_element_108.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 109
line_element_109 = Line(screen, 233, 293, 240, 282)
line_element_109.thickness(3)
line_element_109.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 110
text_element_110 = Text(screen, "Speed Ratio", 221, 257)
text_element_110.color(Color(panelMateColorTo24Bit(7)))
text_element_110.size(12)

# Visual Order 112
line_element_112 = Line(screen, 290, 283, 290, 317)
line_element_112.thickness(3)
line_element_112.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 113
line_element_113 = Line(screen, 280, 303, 288, 315)
line_element_113.thickness(3)
line_element_113.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 114
line_element_114 = Line(screen, 292, 315, 299, 304)
line_element_114.thickness(3)
line_element_114.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 116
line_element_116 = Line(screen, 347, 286, 347, 320)
line_element_116.thickness(3)
line_element_116.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 117
line_element_117 = Line(screen, 348, 283, 356, 295)
line_element_117.thickness(3)
line_element_117.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 118
line_element_118 = Line(screen, 340, 294, 347, 283)
line_element_118.thickness(3)
line_element_118.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 119
text_element_119 = Text(screen, "Speed Ratio", 325, 257)
text_element_119.color(Color(panelMateColorTo24Bit(7)))
text_element_119.size(12)

# Visual Order 121
line_element_121 = Line(screen, 396, 283, 396, 317)
line_element_121.thickness(3)
line_element_121.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 122
line_element_122 = Line(screen, 387, 304, 395, 316)
line_element_122.thickness(3)
line_element_122.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 123
line_element_123 = Line(screen, 397, 316, 404, 305)
line_element_123.thickness(3)
line_element_123.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 125
line_element_125 = Line(screen, 453, 280, 453, 314)
line_element_125.thickness(3)
line_element_125.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 126
line_element_126 = Line(screen, 453, 280, 461, 292)
line_element_126.thickness(3)
line_element_126.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 127
line_element_127 = Line(screen, 445, 291, 452, 280)
line_element_127.thickness(3)
line_element_127.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 128
text_element_128 = Text(screen, "Speed Ratio", 430, 257)
text_element_128.color(Color(panelMateColorTo24Bit(7)))
text_element_128.size(12)

# Visual Order 130
line_element_130 = Line(screen, 501, 282, 501, 316)
line_element_130.thickness(3)
line_element_130.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 131
line_element_131 = Line(screen, 492, 301, 500, 313)
line_element_131.thickness(3)
line_element_131.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 132
line_element_132 = Line(screen, 503, 313, 510, 302)
line_element_132.thickness(3)
line_element_132.color(Color(panelMateColorTo24Bit(0)))

# Visual Order 133
line_element_133 = Line(screen, 210, 255, 210, 325)
line_element_133.thickness(1)
line_element_133.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 134
line_element_134 = Line(screen, 420, 255, 420, 325)
line_element_134.thickness(1)
line_element_134.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 135
line_element_135 = Line(screen, 315, 255, 315, 325)
line_element_135.thickness(1)
line_element_135.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 136
line_element_136 = Line(screen, 106, 255, 106, 325)
line_element_136.thickness(1)
line_element_136.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 137
line_element_137 = Line(screen, 2, 325, 526, 325)
line_element_137.thickness(1)
line_element_137.color(Color(panelMateColorTo24Bit(7)))

# Visual Order 138
text_element_138 = Text(screen, "INC", 14, 307)
text_element_138.color(Color(panelMateColorTo24Bit(0)))
text_element_138.size(12)

# Visual Order 139
text_element_139 = Text(screen, "DEC", 63, 282)
text_element_139.color(Color(panelMateColorTo24Bit(0)))
text_element_139.size(12)

# Visual Order 140
text_element_140 = Text(screen, "INC", 123, 306)
text_element_140.color(Color(panelMateColorTo24Bit(0)))
text_element_140.size(12)

# Visual Order 141
text_element_141 = Text(screen, "INC", 229, 304)
text_element_141.color(Color(panelMateColorTo24Bit(0)))
text_element_141.size(12)

# Visual Order 142
text_element_142 = Text(screen, "INC", 335, 304)
text_element_142.color(Color(panelMateColorTo24Bit(0)))
text_element_142.size(12)

# Visual Order 143
text_element_143 = Text(screen, "INC", 443, 301)
text_element_143.color(Color(panelMateColorTo24Bit(0)))
text_element_143.size(12)

# Visual Order 144
text_element_144 = Text(screen, "DEC", 172, 280)
text_element_144.color(Color(panelMateColorTo24Bit(0)))
text_element_144.size(12)

# Visual Order 145
text_element_145 = Text(screen, "DEC", 279, 280)
text_element_145.color(Color(panelMateColorTo24Bit(0)))
text_element_145.size(12)

# Visual Order 146
text_element_146 = Text(screen, "DEC", 384, 281)
text_element_146.color(Color(panelMateColorTo24Bit(0)))
text_element_146.size(12)

# Visual Order 147
text_element_147 = Text(screen, "DEC", 490, 280)
text_element_147.color(Color(panelMateColorTo24Bit(0)))
text_element_147.size(12)

# Visual Order 148
line_element_148 = Line(screen, 185, 315, 192, 304)
line_element_148.thickness(3)
line_element_148.color(Color(panelMateColorTo24Bit(0)))

## Visual Order 150
#text_element_150 = Text(screen, "18 FORWARD", 22, 339)
#text_element_150.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_150.size(12)
#text_element_150.visible(plc_references['%M0810'])
#
## Visual Order 151
#text_element_151 = Text(screen, "18 REVERSE", 22, 339)
#text_element_151.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_151.size(12)
#text_element_151.visible(plc_references['%M0810'])
#
## Visual Order 153
#text_element_153 = Text(screen, "18 FORWARD", 130, 339)
#text_element_153.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_153.size(12)
#text_element_153.visible(plc_references['%M0811'])
#
## Visual Order 154
#text_element_154 = Text(screen, "18 REVERSE", 130, 339)
#text_element_154.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_154.size(12)
#text_element_154.visible(plc_references['%M0811'])
#
## Visual Order 156
#text_element_156 = Text(screen, "18 FORWARD", 236, 339)
#text_element_156.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_156.size(12)
#text_element_156.visible(plc_references['%M0812'])
#
## Visual Order 157
#text_element_157 = Text(screen, "18 REVERSE", 236, 339)
#text_element_157.color(Color(panelMateColorTo24Bit(Normal)))
#text_element_157.size(12)
#text_element_157.visible(plc_references['%M0812'])

fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)
    if (screen.size() == (-1, -1)): # exit when screen closes
        break
