import os
import pandas as pd
from measure_compression import compare_compression

# loop through the files in to_encode
directory = "text_files/to_encode"
compression_stats = pd.DataFrame(columns=["filename", "bit_compression", "encoded_size", "encoding_time", "decoding_time", "compression_ratio", "saving_percentage", "correct_compression"])
for filename in os.listdir(directory):
    print(f"Measuring compression stats for {filename}")
    # call the compare_compression function
    print("Bits")
    compression_stats.loc[len(compression_stats.index)] = [filename, 'Bits'] + list(compare_compression(filename, 8, 1024, 2048, True))
    print("String")
    compression_stats.loc[len(compression_stats.index)] = [filename, 'String'] + list(compare_compression(filename, 8, 1024, 2048, False))
# save the dataframe to a csv file
compression_stats.to_csv("compression_stats.csv")