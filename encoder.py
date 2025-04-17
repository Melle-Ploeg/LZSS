from bitarray import bitarray


def encode_lempel_ziv_bits(filename, min_window, look_ahead_size, search_buffer_size):
    file = open(f"text_files/to_encode/{filename}", 'r', errors='ignore', encoding='utf-8')

    input_string = str(file.read())
    file.close()

    input_string = input_string.encode('utf-8')
    output_buffer = bitarray()

    search_buffer = bytearray()

    string_pointer = 0

    while string_pointer < len(input_string):
        looked = False
        while len(search_buffer) > search_buffer_size:
            search_buffer.pop(0)
        if string_pointer == len(input_string) - 1:
            output_buffer.append(False) # flags that this is a normal character
            output_buffer.frombytes(bytes([input_string[string_pointer]])) # add the byte
            break
        in_input = string_pointer + min_window
        if in_input < len(input_string):
            looking_at = input_string[string_pointer:in_input]
            while looking_at in search_buffer and in_input - string_pointer <= look_ahead_size:
                looked = True
                in_input += 1
                looking_at = input_string[string_pointer:in_input]
        else:
            looking_at = input_string[string_pointer:]
        if looked:
            if in_input <= len(input_string):
                looking_at = looking_at[:-1]
                in_input -= 1
            occurrence_index = search_buffer.index(looking_at)
            length = len(looking_at)
            output_buffer.append(True) # flags that this is a pointer
            offset = len(search_buffer) - occurrence_index
            output_buffer.frombytes(offset.to_bytes(2, 'big')) # add the offset
            output_buffer.frombytes(length.to_bytes(2, 'big')) # add the length
            search_buffer.extend(looking_at)
            string_pointer = in_input
        else:
            output_buffer.append(False) # flags that this is a normal character
            output_buffer.frombytes(bytes([input_string[string_pointer]])) # add the byte
            search_buffer.append(input_string[string_pointer])
            string_pointer += 1

    f = open(f"text_files/encoded/{filename}_encodedbits", 'wb')
    output_buffer.fill()
    output_buffer.tofile(f)


def encode_lempel_ziv_string(filename, min_window, look_ahead_size, search_buffer_size):
    file = open(f"text_files/to_encode/{filename}", 'r', errors='ignore', encoding='utf-8')

    input_string = str(file.read())
    file.close()

    string_pointer = 0

    output_string = ""
    search_buffer = ""

    min_window = min_window
    look_ahead_size = look_ahead_size
    search_buffer_size = search_buffer_size

    while string_pointer < len(input_string):
        looked = False
        while len(search_buffer) > search_buffer_size:
            search_buffer = search_buffer[1:]
        if string_pointer == len(input_string) - 1:
            output_string += input_string[string_pointer]
            break
        in_input = string_pointer + min_window
        if in_input < len(input_string):
            looking_at = str(input_string[string_pointer:in_input])
            while looking_at in search_buffer and in_input - string_pointer <= look_ahead_size:
                looked = True
                in_input += 1
                looking_at = input_string[string_pointer:in_input]
        else:
            looking_at = str(input_string[string_pointer:])
        if looked:
            if in_input <= len(input_string):
                looking_at = looking_at[:-1]
                in_input -= 1
            occurence_index = search_buffer.index(looking_at)
            length = len(looking_at)
            output_string += f"({len(search_buffer) - occurence_index},{length})"
            search_buffer += looking_at
            string_pointer = in_input
        else:
            output_string += input_string[string_pointer]
            search_buffer += input_string[string_pointer]
            string_pointer += 1

    f = open(f"text_files/encoded/{filename}_encoded", 'w', encoding='utf-8')
    f.write(output_string)

    f.close()