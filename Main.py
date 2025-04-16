import os
import time
import numpy as np
import pandas as pd
from measure_compression import compare_compression

# loop through the files in to_encode
directory = "text_files/to_encode"
compression_stats = pd.DataFrame(columns=["filename", "encoding_time", "decoding_time", "compression_ratio", "saving_percentage"])
for filename in os.listdir(directory):
    if filename != 'bible':
        print(f"Measuring compression stats for {filename}")
        # call the compare_compression function
        compression_stats.loc[len(compression_stats.index)] = [filename] + list(compare_compression(filename, 6, 256, 256))

# save the dataframe to a csv file
compression_stats.to_csv("compression_stats.csv")