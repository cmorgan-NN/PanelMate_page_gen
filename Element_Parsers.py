# Different element parsers live here
# Yo, there is waaay too much voodoo in here
class Element_Parsers:
    def element_parser(key, next_key, line):
        if (line.find(key) == 0):  
            line = line.lstrip(key)
            if line[0] != ' ':
                #check to make sure value doesn't have leading space
                value = line[0:(line.find(next_key))].strip()
        else:
            raise Exception("Parse Error: key not at position 0")

        return {'element' : {key[:len(key) - 2] : value}, 
                'remaining_line' : line[line.find(next_key):]}