# Read the encoded and the decoded file
import os.path

original_size = os.path.getsize("text_files/to_encode/lyric_harderbetterfasterstronger")
encoded_size = os.path.getsize("text_files/encoded/lyric_harderbetterfasterstronger_encoded")

print(original_size, encoded_size)
print("The file was compressed by" , 100 * abs((encoded_size-original_size))/original_size, "%")