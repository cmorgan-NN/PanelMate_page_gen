# TODO: Finish this!
# Renderer for variable sized indicator

# from Renderer_Utility import *


class Variable_Sized_Readout:

    def render_visual_order(visual_order):

        # Visual Order String Variables
        vo = visual_order["Visual Order"]
        x_origin = visual_order["X Origin"]
        y_origin = visual_order["Y Origin"]
        x_size = visual_order["X Size"]
        y_size = visual_order["Y Size"]
        refresh_affected_graphics_online = visual_order[
            "Refresh Affected Graphics Online"
        ]
        enable_cond_visibility = visual_order["Enable Conditional Visibility"]
        visibility_expression = (
            visual_order["Visibility Expression"].lstrip("[").rstrip("]")
        )
        alarm_device_name = visual_order["Alarm Device Name"]

        vo_type_string = "indicator_element_"  # this is dirty... TODO: fix this

        return_list = []
        reference_list = []

        return_list.extend(["# Visual Order " + vo])
        return_list.extend(
            [
                vo_type_string
                + vo
                + " = Text(screen, "
                + "plc_references['"
                + value_expression
                + "'], "
                + x_origin
                + ", "
                + y_origin
                + ")"
            ]
        )

        return_list.extend(
            [
                vo_type_string
                + vo
                + ".color(Color(panelMateColorTo24Bit("
                + foreground_color
                + ")))"
            ]
        )
        return_list.extend([vo_type_string + vo + ".size(" + READOUT_FONT_SIZE + ")"])

        #        if enable_cond_visibility == 'Yes':
        #            eval_return_list, visibility_expression = Renderer_Utility.visibility_expression_evaluator(vo, vo_type_string, visibility_expression)
        #            return_list.extend(eval_return_list)
        #
        #        if visibility_expression != '':
        #            reference_list.extend([visibility_expression])
        reference_list.extend([value_expression])

        return_list.extend([""])

        return (return_list, reference_list)
