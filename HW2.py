import re

def extract_vowel_words(text):
    words = re.findall(r'\b[aeiouAEIOU]\w+', text)
    return words

input_text = "I am learning programming in python. It's very exciting and interesting."

result = extract_vowel_words(input_text)
print(result)
input("press any key to close window")
