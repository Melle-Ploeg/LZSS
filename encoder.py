# Read the file

def encode_lempel_ziv_string(filename, min_window, look_ahead_size, search_buffer_size):
    file = open(f"text_files/to_encode/{filename}", 'r')

    input_string = str(file.read())
    file.close()

    string_pointer = 0

    input_had = ""
    output_string = ""

    min_window = min_window
    look_ahead_size = look_ahead_size # 32 is the max window size
    search_buffer_size = search_buffer_size

    while string_pointer < len(input_string):
        looked = False
        if len(input_had) > search_buffer_size:
            search_buffer = input_had[len(input_had)-search_buffer_size:len(input_had)]
        else:
            search_buffer = input_had
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
            input_had += looking_at
            string_pointer = in_input
        else:
            output_string += input_string[string_pointer]
            input_had += input_string[string_pointer]
            string_pointer += 1

    print(output_string)
    f = open(f"text_files/encoded/{filename}_encoded", 'w')
    f.write(output_string)

    f.close()