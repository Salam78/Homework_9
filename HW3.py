import re

def split_string(text, delimiters):
    regex_pattern = '|'.join(map(re.escape, delimiters))
    tokens = re.split(regex_pattern, text)
    return tokens

input_text = "I am learning programming in python, and I am also learning English. It's very exciting and interesting!"
input_delimiters = [',', '!', '?']

result = split_string(input_text, input_delimiters)
print(result)
input("press any key to close window")
