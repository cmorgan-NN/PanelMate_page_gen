#Utility methods common to all renderers

class Renderer_Utility:
    def visibility_expression_evaluator(visual_order, visual_order_type_string, visibility_expression): #needs a better name
        #processes a visual order's visibility expression and retruns list containing
        #proper strings to build the expression's functionality into the rendered code
    
        return_list = []

        #case of "= 0" or "= 1"
        if '] =' in visibility_expression:
            if visibility_expression[len(visibility_expression) - 1] == '0':
                # [visibility_expression] = 0
                visibility_expression = visibility_expression[:visibility_expression.find('] =')]
                return_list.extend([visual_order_type_string +
                                    visual_order +
                                    ".visible(not plc_references['" +
                                    visibility_expression + "'])"])
            else:
                # [visibility_expression] = 1
                visibility_expression = visibility_expression[:visibility_expression.find('] =')]
                return_list.extend([visual_order_type_string + 
                                    visual_order +
                                    ".visible(plc_references['" +
                                    visibility_expression + "'])"])
        else:
            return_list.extend([visual_order_type_string + 
                            visual_order +
                            ".visible(plc_references['" +
                            visibility_expression +
                            "'])"])

        return (return_list, visibility_expression)