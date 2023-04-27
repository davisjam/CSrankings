import csv
import sys
import os

# Determine input and output filenames
input_filename = sys.argv[1]
output_filename = input_filename.replace('csrankings-', 'csrankings-ece-')

# Open input file
with open(input_filename, newline='') as input_file:
    reader = csv.reader(input_file)
    header = next(reader)
    output_rows = [header]

    # Loop through each row
    for row in reader:
        # Check if the 3rd field is "ECE"
        if row[2] == "ECE":
            # Replace the 2nd field with "Purdue University-ECE"
            row[1] = "Purdue University-ECE"

        output_rows.append(row)

# Write output to file
with open(output_filename, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_rows)

