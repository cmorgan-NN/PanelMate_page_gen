# Renderer for static grapic data line elements

def render_visual_order(visual_order):
    
    vo = visual_order['Visual Order']
    x_origin = visual_order['X Origin']
    y_origin = visual_order['Y Origin']
    end_x = visual_order['End X']
    end_y = visual_order['End Y']
    pen_width = visual_order['Pen Width']
    pen_color = visual_order['Pen Color']
    
    return_list = []

    return_list.extend(['# Visual Order ' + vo])
    return_list.extend(['lineEl' + vo + ' = Line(screen, ' + x_origin +
                        ', ' + y_origin +
                        ', ' + end_x +
                        ', ' + end_y + ')'])
    return_list.extend(['lineEl' + vo + '.thickness(' + pen_width + ')'])
    return_list.extend(['lineEl' + vo + '.color(Color(panelMateColorTo24Bit(' + 
                        pen_color + ')))']) 
    return_list.extend([''])
    
    return return_list
