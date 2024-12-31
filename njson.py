
'''
╭━╮╱╭╮╱╭┳━━━┳━━━┳━╮╱╭╮
┃┃╰╮┃┃╱┃┃╭━╮┃╭━╮┃┃╰╮┃┃
┃╭╮╰╯┃╱┃┃╰━━┫┃╱┃┃╭╮╰╯┃
┃┃╰╮┃┣╮┃┣━━╮┃┃╱┃┃┃╰╮┃┃
┃┃╱┃┃┃╰╯┃╰━╯┃╰━╯┃┃╱┃┃┃
╰╯╱╰━┻━━┻━━━┻━━━┻╯╱╰━╯
'''

import os
import ast


def true_type(var) -> int | float | str | bool | dict:
    try:
        return int(var)
    except ValueError:
        pass
    try:
        return float(var)
    except ValueError:
        pass
    try:
        parsed_list = ast.literal_eval(var)
        if isinstance(parsed_list, list):
            return parsed_list
    except (ValueError, SyntaxError):
        pass
    try:
        parsed_dict = ast.literal_eval(var)
        if isinstance(parsed_dict, dict):
            return parsed_dict
    except (ValueError, SyntaxError):
        pass

    if var == "true":
        return True
    if var == "false":
        return False
        
    if var == "null":
        return None

    return str(var[1:-1])


def true_type_json(var):
    if var == True and isinstance(var, bool):
        return "true"
    if var == False:
        return "false"
    if var == None:
        return "null"
    if isinstance(var, str):
        return f'"{var}"'
    if isinstance(var, list):
        return f'[{", ".join(str(true_type_json(v)) for v in var)}]'
    if isinstance(var, dict):
        items = [f'"{k}": {true_type_json(v)}' for k, v in var.items()]
        return f'{{{", ".join(items)}}}'

    return var

class njson:
    def load(json: str) -> dict:
        lines_array = []
        res_dict = {}
        if ".json" in json and os.path.exists(json):
            with open(json, 'r') as file:
                for lines in file:
                    if lines.strip() == "{" or lines.strip() == "}":
                        pass
                    else:
                        lines_array += [lines.strip()]
        else:
            raise "FileError"
        
        for part in lines_array:
            a = part[1:].find('"')
            b = part[a:].find(':')
            if part[-1] == ",":
                res_dict[part[1:a+1]] = true_type(part[b+3:-1])
            else:
                res_dict[part[1:a+1]] = true_type(part[b+3:])
            

        return res_dict

    # easy ways for weaklings    
    #
    # def _load(json):
    #     d = ""
    #     with open(json, 'r') as f:
    #         for lines in f:
    #             d+=lines.strip()
    #     return ast.literal_eval(d)

    def write(json: str, ur_dict: dict) -> None:
        if ".json" in json and os.path.exists(json):
            with open(json, 'w') as f:
                f.write("{\n")
                for index, (key, value) in enumerate(ur_dict.items()):
                    f.write(f'  "{key}": {true_type_json(value)}')
                    if index < len(ur_dict) - 1:
                        f.write(",\n")
                    else:
                        f.write("\n") 
                    
                f.write("}")

        else:
            raise "FileError"

    def add(json: str, ur_dict: str) -> None:
        if ".json" in json and os.path.exists(json):
            a = []
            with open(json, 'r') as f:
                for i in f:
                    a.append(i)

            a[-1] = ""
            a[len(a)-2] = '  ' + a[len(a)-2].strip() + ',\n'

            with open(json, 'w') as f:
                for i in a:
                    f.write(i)
                for index, (key, value) in enumerate(ur_dict.items()):
                    f.write(f'  "{key}": {true_type_json(value)}')
                    if index < len(ur_dict) - 1:
                        f.write(",\n")
                    else:
                        f.write("\n") 
                
                f.write("}")

        else:
            raise "FileError"

