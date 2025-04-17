from bitarray import bitarray


def decode_lempel_ziv_bits(filename):
    file = open(f"text_files/encoded/{filename}_encodedbits", 'rb')

    text = bitarray()
    text.fromfile(file)
    file.close()

    pointer = 0

    decoded_text = []
    while len(text) - pointer >= 9: # if there are less than 9 bits it's all padding
        if text[pointer]: # this means we have a (offset, length) pair
            pointer += 1
            offset = int.from_bytes(text[pointer:pointer+16].tobytes(), 'big')
            pointer += 16
            length = int.from_bytes(text[pointer:pointer+16].tobytes(), 'big')
            pointer += 16
            decoded_text += decoded_text[len(decoded_text) - offset:-offset+length+len(decoded_text)]
        else:
            pointer += 1
            decoded_text.append(text[pointer:pointer+8].tobytes())
            pointer += 8
    f = open(f"text_files/decoded/{filename}_decodedbits", 'wb')
    f.write(b''.join(decoded_text))
    f.close


def decode_lempel_ziv_string(filename):
    file = open(f"text_files/encoded/{filename}_encoded", 'r', encoding='utf-8')

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
    f = open(f"text_files/decoded/{filename}_decoded", 'w', encoding='utf8')
    f.write(decoded_text)
    f.close()
