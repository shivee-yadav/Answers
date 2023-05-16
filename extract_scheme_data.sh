#!/bin/bash

url="http://amfiindia.com/spages/NAVAll.txt"
output_file="scheme_data.csv"

# Fetch the data from the URL using curl and save it to a temporary file
temp_file=$(mktemp)
curl -s "$url" -o "$temp_file"

# Extract the Scheme Name and Asset Value fields and save them to the CSV file
awk -F ';' '{print $4 "," $5}' "$temp_file" > "$output_file"

# Clean up the temporary file
rm "$temp_file"

echo "Extraction completed. CSV file saved as $output_file"
