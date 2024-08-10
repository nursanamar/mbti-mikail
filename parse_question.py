import re
import os

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,"question.txt")

text = ""

with open(file_path) as file:
    lines = file.readlines()
    text = "".join(lines)

def parse_option(option):
    regex = r"([a-z])\.\s*(.*)"
    matches = re.finditer(regex, option, re.MULTILINE)
    value = ""
    label = ""
    
    for match in matches:
        value = match.group(1)
        label = match.group(2)
    
    return value, label
        

def parse_options(options):
    result = []
    for option in options:
        result.append(parse_option(option))
    
    return result
        

parsed_questions = []

for question in text.split("\n\n\n"):
    parsed = question.split("\n")
    question_text = parsed[0]
    
    options = parse_options(parsed[1:])
    
    parsed_questions.append((question_text, options))

