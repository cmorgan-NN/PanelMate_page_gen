# Renderer for static grapic data rectangle elements
class Static_Graphic_Data_Rectangle:
    def render_visual_order(visual_order):
        vo = visual_order["Visual Order"]
        x_origin = visual_order["X Origin"]
        y_origin = visual_order["Y Origin"]
        size_x = visual_order["Size X"]
        size_y = visual_order["Size Y"]
        pen_width = visual_order["Pen Width"]
        pen_color = visual_order["Pen Color"]
        fill_color = visual_order["Fill Color"]

        return_list = []

        return_list.extend(["# Visual Order " + vo])
        return_list.extend(
            [
                "rectangle_element_"
                + vo
                + " = Rectangle(screen, "
                + x_origin
                + ", "
                + y_origin
                + ", "
                + size_x
                + " - 1 "
                + ", "
                + size_y
                + " - 1 "
                + ")"
            ]
        )
        return_list.extend(
            [
                "rectangle_element_"
                + vo
                + ".color(Color(panelMateColorTo24Bit("
                + fill_color
                + ")))"
            ]
        )  # fill_color
        return_list.extend(
            [
                "rectangle_element_"
                + vo
                + ".border(Color(panelMateColorTo24Bit("
                + pen_color
                + ")))"
            ]
        )  # pen_color
        return_list.extend(
            ["rectangle_element_" + vo + ".border_width(" + pen_width + ")"]
        )  # pen_width
        return_list.extend(["if RECTANGLES_IN_BACK:"])
        return_list.extend(["    rectangle_element_" + vo + ".back()"])
        return_list.extend([""])

        return return_list
