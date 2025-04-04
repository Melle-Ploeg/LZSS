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
file = open("text_files/to_encode/sam_i_am")

input_string = str(file.read())

bytetjes = bytearray(input_string, 'utf-8')


string_pointer = 0
past_inputs = []
string_to_check = ''


def substitute_occurrence(occ_i, length):
    return f"({occ_i},{length})"

locations = {}
output_string = ""

while string_pointer < len(input_string):
    current_val = input_string[string_pointer]
    if (string_to_check+current_val) in ''.join(past_inputs):
        string_to_check += current_val
        occurrences = past_inputs.index(current_val)
    else:
        # Verander dit voor oprechte LZSS implementatie
        if len(string_to_check) > 4:
            print(past_inputs)
            print(string_to_check)
            occurrence_index = input_string.index(string_to_check)
            output_string += substitute_occurrence(occurrence_index, len(string_to_check))
        else:
            output_string += string_to_check+current_val
        string_to_check = ''
    string_pointer += 1
    past_inputs.append(current_val)

print(output_string)
f = open("text_files/encoded/sam_i_am_encoded2", 'w')
f.write(output_string)
f.close()
