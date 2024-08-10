import os

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,"mbti_types.txt")

text = ""

with open(file_path) as file:
    lines = file.readlines()
    text = "".join(lines)


def parse_type(type):
    parsed = type.split("\n")
    name = parsed[0]
    desc = parsed[1]
    
    return name,desc 

mbti_types = {}

for type in text.split("\n\n"):
    name, desc = parse_type(type)
    mbti_types[name] = desc
