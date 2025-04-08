import os.path

# Pseudocode:
# while input is not empty do
#     match := longest repeated occurrence of input that begins in window
#
#     if match exists then
#         d := distance to start of match
#         l := length of match
#         c := char following match in input
#     else
#         d := 0
#         l := 0
#         c := first char of input
#     end if
#
#     output (d, l, c)
#
#     discard l + 1 chars from front of window
#     s := pop l + 1 chars from front of input
#     append s to back of window
# repeat

# Read the file
file = open("text_files/to_encode/lyric_aroundtheworld")

input_string = str(file.read())
file.close()

string_pointer = 0

input_had = ""
output_string = ""

min_window = 4
look_ahead_size = 256 # 32 is the max window size
search_buffer_size = 256

while string_pointer < len(input_string):
    looked = False
    if string_pointer == len(input_string) - 1:
        output_string += input_string[string_pointer]
        break
    in_input = string_pointer + min_window
    if in_input < len(input_string):
        looking_at = str(input_string[string_pointer:in_input])
        while looking_at in search_buffer and in_input - string_pointer <= look_ahead_size:
            looked = True
            looking_at = input_string[string_pointer:in_input]
            in_input += 1
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
        string_pointer = in_input - 1
    else:
        output_string += input_string[string_pointer]
        input_had += input_string[string_pointer]
        string_pointer += 1


# bytetjes = bytearray(input_string, 'utf-8')
#
#
# string_pointer = 0
# past_inputs = []
# string_to_check = ''
#
#
# def substitute_occurrence(occ_i, length):
#     return f"({occ_i},{length})"
#
# locations = {}
# output_string = ""
#
# while string_pointer < len(input_string):
#     current_val = input_string[string_pointer]
#     if (string_to_check+current_val) in ''.join(past_inputs):
#         string_to_check += current_val
#         occurrences = past_inputs.index(current_val)
#     else:
#         # Verander dit voor oprechte LZSS implementatie
#         if len(string_to_check) > 4:
#             print(past_inputs)
#             print(string_to_check)
#             occurrence_index = input_string.index(string_to_check)
#             output_string += substitute_occurrence(occurrence_index, len(string_to_check))
#         else:
#             output_string += string_to_check+current_val
#         string_to_check = ''
#     string_pointer += 1
#     past_inputs.append(current_val)

print(output_string)
f = open("text_files/encoded/lyric_aroundtheworld_encoded", 'w')
f.write(output_string)
f.close()
