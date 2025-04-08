import regex as re

file = open("text_files/encoded/lyric_aroundtheworld_encoded")

text = str(file.read())

decoded_text = ""

string_pointer = 0
while string_pointer < len(text):
    if text[string_pointer] == "(":
        string_pointer += 1
        digits = ""
        text_pointer = (0, 0)
        while text[string_pointer].isdigit():
            digits += text[string_pointer]
            string_pointer += 1
        if digits == "":
            decoded_text += "("
            continue
        text_pointer = (int(digits), 0)
        if text[string_pointer] == ",":
            string_pointer += 1
        else:
            decoded_text += "(" + digits
            decoded_text += text[string_pointer]
            string_pointer += 1
            continue
        digits = ""
        while text[string_pointer].isdigit():
            digits += text[string_pointer]
            string_pointer += 1
        if digits == "":
            decoded_text += "(" + str(text_pointer[0]) + ","
            continue
        text_pointer = (text_pointer[0], int(digits))
        if text[string_pointer] == ")":
            decoded_text += decoded_text[text_pointer[0]:(text_pointer[0] + text_pointer[1])]
            string_pointer += 1
        else:
            decoded_text += "(" + str(text_pointer[0]) + "," + str(text_pointer[1])
            continue
    else:
        decoded_text += text[string_pointer]
        string_pointer += 1

print(decoded_text)