# Static Graphic Data Line Element parser
from Sub_Parsers import *
from Parser_Utility import *


class Static_Graphic_Data_Line:

    # Function to parse a list of Visual Orders and their elements into a dictionary
    def parse_visual_orders(static_graphic_data):

        # Visual Order String Variables
        elements = [
            "Visual Order",
            "X Origin",
            "Y Origin",
            "End X",
            "End Y",
            "Pen Width",
            "Pen Color",
        ]

        visualOrderElementsList = Parser_Utility.remove_table_headings(
            elements, static_graphic_data
        )

        visualOrders = {}
        for line in visualOrderElementsList:
            visualOrder = {}

            # for EOF that are missing the newline
            if line[len(line) - 1] != "\n":
                line = line + "\n"

            # This voodoo should parse out anything in an element table
            for member in enumerate(elements):
                parsed_element = Sub_Parsers.table_parser(member[1], member[0], line)
                visualOrder.update(parsed_element)

            # Create dictionary of all VS_Indicator Visual Order elements
            visualOrders.update(
                {visualOrder["Visual Order"]: visualOrder}
            )  # wow, thats a confusing line!

        return visualOrders
