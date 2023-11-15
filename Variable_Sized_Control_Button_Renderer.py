# Renderer for variable sized control button elements

from Renderer_Utility import *

class Variable_Sized_Control_Button:

    def render_visual_order(visual_order):

        vo = visual_order['Visual Order']
        x_origin = visual_order['X Origin']
        y_origin = visual_order['Y Origin']
        x_size = visual_order['X Size']
        y_size = visual_order['Y Size']
        # refresh_affected_graphics_online = visual_order['Refresh Affected Graphics Online']
        enable_cond_visibility = visual_order['Enable Conditional Visibility']
        visibility_expression = visual_order['Visibility Expression'].lstrip('[').rstrip(']')
        lens_color = visual_order['Lens Color']
        control_type = visual_order['Control Type']
        
        if 'Reference' in visual_order:
            reference = visual_order['Reference']
        elif 'Expression' in visual_order:
            expression = visual_order['Expression']

        vo_type_string = 'control_button_element_' #this is dirty... TODO: fix this

        return_list = []
        reference_list = []

        return_list.extend(['# Visual Order ' + vo + ' (' + control_type + ')'])
        if locals().get('reference'):
            return_list.extend(['# Reference: ' + reference])
            reference_list.extend([reference.lstrip('[').rstrip(']')]) 
        elif locals().get('expression'):
            return_list.extend(['# Expression: ' + expression])
        return_list.extend([vo_type_string + vo + ' = Rectangle(screen, ' + x_origin +
                            ', ' + y_origin +
                            ', ' + x_size +
                            ', ' + y_size + ')'])

        return_list.extend([vo_type_string + vo + '.color(Color(panelMateColorTo24Bit(' + 
                            lens_color + ')))'])

        return_list.extend([vo_type_string + vo + '.border_width(' + '1' + ')'])
        return_list.extend([vo_type_string + vo + '.border(Color(panelMateColorTo24Bit(' +
                            '0' + ')))'])
        if enable_cond_visibility == 'Yes':
            eval_return_list, visibility_expression = Renderer_Utility.visibility_expression_evaluator(vo, vo_type_string, visibility_expression) 
            return_list.extend(eval_return_list)
        
        if visibility_expression != '':
            reference_list.extend([visibility_expression]) 

        return_list.extend([''])

        return (return_list, reference_list)