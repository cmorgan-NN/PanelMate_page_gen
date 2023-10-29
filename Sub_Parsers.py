# Different element parsers live here
# Yo, there is waaay too much voodoo in here

class Sub_Parsers:
    def element_parser(key, next_key, line):

        #if there is a value associated with the element
        if (line.find(key) == 0):  
            line = line[len(key) + 1:]
            if line == '' or line[0] != ' ':
                #check to make sure value doesn't have leading space
                value = line[0:(line.find(next_key.strip()))].strip()
            
            else:
                raise Exception("Parse Error: value not at position 0")

        else:
            raise Exception("Parse Error: key not at position 0")

        return {'element' : {key[:len(key) - 1] : value}, 
                'remaining_line' : line[line.find(next_key):]}
    
    
    #for parsing static graphic rpc tables
    def table_parser(key, key_index, line):

        line = enumerate(line.split(' '))
        for element in line:
            index, element_value = element
            if index == key_index:
                value = element_value.strip()
                break

        return {key : value}