import os
import json

__all__ = ["char_number", "char_type"]

current_dir = os.path.dirname(os.path.abspath(__file__))

char_number = json.load(open((os.path.join(current_dir, 'char_number.json')), "r"))
char_type = json.load(open((os.path.join(current_dir, 'char_type.json')), "r"))