import pandas as pd
import os
import sys
def main():
    if len(sys.argv) < 2:
        print("Please provide one or more CSV files as arguments.")
        sys.exit(1)

    input_filenames = sys.argv[1:]

# Create an empty list to store the DataFrames
    data_frames = []

# Iterate over the input files
    for input_filename in input_filenames:
    # Read the CSV file into a DataFrame
        df = pd.read_csv(input_filename, header=0,  error_bad_lines=False)
    # Add a new column with the filename
        df["filename"] = os.path.basename(input_filename)
    # Append the DataFrame to the list
        data_frames.append(df)

# Concatenate all the DataFrames into a single DataFrame
    result = pd.concat(data_frames, ignore_index=True)
    
    cols = list(result.columns)
    cols.remove("filename")
    result = result[cols + ["filename"]]


# Write the DataFrame to stdout
    result.to_csv(sys.stdout, index=False)

if __name__ == '__main__':
    main()