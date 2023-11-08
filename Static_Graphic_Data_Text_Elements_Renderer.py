# Renderer for static graphic data text elements
font_size = 12 #default font size
class Static_Graphic_Data_Text:

    def render_visual_order(visual_order):

        vo = visual_order['Visual Order']
        x_origin = visual_order['X Origin']
        y_origin = visual_order['Y Origin']
        # refresh_affected_graphics_online = visual_order['Refresh Affected Graphics Online']
        enable_cond_visibility = visual_order['Enable Cond. Visibility']
        visibility_expression = visual_order['Visibility Expression'].lstrip('[').rstrip(']')
        # font = visual_order['Font']
        foreground_color = visual_order['Foreground Color']
        # background_color = visual_order['Background Color']
        text = visual_order['Text']

        return_list = []
        reference_list = []

        return_list.extend(['# Visual Order ' + vo])
        return_list.extend(['text_element_' + vo + ' = Text(screen, "' + text +
                            '", ' + x_origin +
                            ', ' + y_origin + ')'])
        return_list.extend(['text_element_' + vo + 
                            '.color(Color(panelMateColorTo24Bit(' + foreground_color + ')))'])
        return_list.extend(['text_element_' + vo + '.size(' + str(font_size) + ')'])
        if enable_cond_visibility == 'Yes':
            return_list.extend(['text_element_' + 
                                vo +
                                ".visible(plc_references['" +
                                visibility_expression +
                                "'])"])
            reference_list.extend([visibility_expression])                            
                
        return_list.extend([''])

        return (return_list, reference_list)
