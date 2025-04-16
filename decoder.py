import regex as re

def decode(filename):
    file = open(f"text_files/encoded/{filename}_encoded", 'r')

    text = str(file.read())

    decoded_text = ""

    string_pointer = 0
    while string_pointer < len(text):
        if text[string_pointer] == "(":
            string_pointer += 1
            digits = ""
            offset = (0, 0)
            while text[string_pointer].isdigit():
                digits += text[string_pointer]
                string_pointer += 1
            if digits == "":
                decoded_text += "("
                continue
            offset = (int(digits), 0)
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
                decoded_text += "(" + str(offset[0]) + ","
                continue
            offset = (offset[0], int(digits))
            if text[string_pointer] == ")":
                decoded_text += decoded_text[len(decoded_text) - offset[0]:(-offset[0] + offset[1] + len(decoded_text))]
                string_pointer += 1
            else:
                decoded_text += "(" + str(offset[0]) + "," + str(offset[1])
                continue
        else:
            decoded_text += text[string_pointer]
            string_pointer += 1
    f = open(f"text_files/decoded/{filename}_decoded", 'w')
    f.write(decoded_text)
    f.close()
