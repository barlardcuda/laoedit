from ..assets.char import *

def convert(input, type="text", engine="encode"):
    if type == "text":
        if engine == "encode":
            return [char_number["encode"].get(char, "?") for char in input]
        elif engine == "decode":
            return [char_number["decode"].get(char, "?") for char in input]
        else:
            return "engine error"
    elif type == "array":
        text = []
        for d in input:
            tps = ""
            if engine == "encode":
                tps = [char_number["encode"].get(char, "?") for char in d]
            elif engine == "decode":
                tps = [char_number["decode"].get(char, "?") for char in d]
            else:
                return "engine error"
                break
            text.append(''.join(tps))
        return text
    else:
        return "type error"