# Renderer for variable sized readout elements

# from Renderer_Utility import *

class Variable_Sized_Readout:

    def render_visual_order(visual_order):

        #Visual Order String Variables
        vo = visual_order['Visual Order']
        x_origin = visual_order['X Origin']
        y_origin = visual_order['Y Origin']
        x_size = visual_order['X Size']
        y_size = visual_order['Y Size']
        font = visual_order['Font']
        deadband_range = visual_order['Deadband Range']
        alarm_ack = visual_order['Alarm Ack']
        refresh_affected_graphics_online = visual_order['Refresh Affected Graphics Online']
        enable_cond_visibility = visual_order['Enable Conditional Visibility']
        visibility_expression = visual_order['Visibility Expression'].lstrip('[').rstrip(']')
        foreground_color = visual_order['Foreground Color']
        background_color = visual_order['Background Color']
        text_direction = visual_order['Text Direction']
        decimal_places = visual_order['Decimal Places']
        control_arrow_position = visual_order['Control Arrow Position']
        control_arrow_display_flag = visual_order['Control Arrow Display Flag']
        alarm_device_name = visual_order['Alarm Device Name']
        value_expression = visual_order['Value Expression'][
            visual_order['Value Expression'].find('%'):
            visual_order['Value Expression'].find('%') + 6]
#        high_alarm_expression = visual_order['High Alarm Expression']
#        low_alarm_expression = visual_order['Low Alarm Expression']

        #Control Definitions
#        input_value_expression = visual_order['Input Value Expression']
#        target_word_address = visual_order['Target Word Address']
#        password_protection = visual_order['Password Protection']

        #Local Variables
        READOUT_FONT_SIZE = '10'

        vo_type_string = 'readout_element_' #this is dirty... TODO: fix this

        return_list = []
        reference_list = []

        return_list.extend(['# Visual Order ' + vo ])
        return_list.extend([vo_type_string + vo + ' = Text(screen, '
                            + "plc_references['" + value_expression + "'], " 
                            + x_origin +
                            ', ' + y_origin + ')'])
#                            ', ' + x_size +
#                           ', ' + y_size + ')'])

        return_list.extend([vo_type_string + vo + '.color(Color(panelMateColorTo24Bit(' + 
                            foreground_color + ')))'])
        return_list.extend([vo_type_string + vo + '.size(' + READOUT_FONT_SIZE + ')'])

#        if enable_cond_visibility == 'Yes':
#            eval_return_list, visibility_expression = Renderer_Utility.visibility_expression_evaluator(vo, vo_type_string, visibility_expression) 
#            return_list.extend(eval_return_list)
#        
#        if visibility_expression != '':
#            reference_list.extend([visibility_expression]) 
        reference_list.extend([value_expression])

        return_list.extend([''])

        return (return_list, reference_list)