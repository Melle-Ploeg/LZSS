# Read the encoded and the decoded file
import os.path
import time

from decoder import decode_lempel_ziv_string, decode_lempel_ziv_bits
from encoder import encode_lempel_ziv_string, encode_lempel_ziv_bits


def compare_compression(filename, min_window=4, look_ahead_size=4096, search_buffer_size=4096, bits=False):
    failed = False
    # Time how long the encoding takes
    if bits:
        start = time.time()
        encode_lempel_ziv_bits(filename, min_window, look_ahead_size, search_buffer_size)
        encoding_time = time.time() - start

        start = time.time()
        decode_lempel_ziv_bits(filename)
        decoding_time = time.time() - start
    else:
        start = time.time()
        encode_lempel_ziv_string(filename, min_window, look_ahead_size, search_buffer_size)
        encoding_time = time.time() - start

        start = time.time()
        decode_lempel_ziv_string(filename)
        decoding_time = time.time() - start

    # ensure that the original and decoded files are the same
    file = open(f"text_files/to_encode/{filename}", 'r', errors='ignore', encoding='utf-8')
    original_text = str(file.read())
    file.close()

    if bits:
        file = open(f"text_files/decoded/{filename}_decodedbits", 'r', errors='ignore', encoding='utf-8')
        decoded_text = str(file.read())
        file.close()
    else:
        file = open(f"text_files/decoded/{filename}_decoded", 'r', errors='ignore', encoding='utf-8')
        decoded_text = str(file.read())
        file.close()

    if (original_text != decoded_text):
        print("Faulty decoding")
        failed = True
    

    original_size = os.path.getsize(f"text_files/to_encode/{filename}")
    if bits:
        encoded_size = os.path.getsize(f"text_files/encoded/{filename}_encodedbits")
    else:
        encoded_size = os.path.getsize(f"text_files/encoded/{filename}_encoded")

    compression_ratio = encoded_size / original_size
    saving_percentage = (original_size - encoded_size) / original_size * 100
    print("Compression time: " + str(round(encoding_time, 2)) + "s")
    print("Decompression time: " + str(round(decoding_time, 2)) + "s")
    print("Compression ratio: " + str(round(compression_ratio, 2)))
    print("Saving percentage: " + str(round(saving_percentage, 2)) + "%")
    return encoded_size, encoding_time, decoding_time, compression_ratio, saving_percentage, not failed
