#!/bin/bash

# Define the output file
output="/Users/manvi/Downloads/merged_sx.csv"

# Check if the output file already exists and remove it to start fresh
if [ -f "$output" ]; then
    rm "$output"
fi

# Initialize a variable to keep track of whether the header has been added to the output file
header_added="no"

# Loop through all CSV files in the current directory
for file in *.csv; do
    # Check if the file variable contains an actual file name
    if [ -f "$file" ]; then
        if [ "$header_added" = "no" ]; then
            # If the header hasn't been added yet, copy the entire file
            cat "$file" > "$output"
            header_added="yes"
        else
            # If the header has been added, skip the first line (header) and append the rest
            tail -n +2 "$file" >> "$output"
        fi
    fi
done

echo "All CSV files have been combined into $output."
