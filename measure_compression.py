# Read the encoded and the decoded file
import os.path

original_size = os.path.getsize("text_files/to_encode/sam_i_am")
encoded_size = os.path.getsize("text_files/encoded/sam_i_am_encoded2")

print(original_size, encoded_size)
print("The file was compressed by" , 100 * encoded_size/original_size, "%")