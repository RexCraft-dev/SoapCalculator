import csv
import json

# Read CSV data
csv_file_path = "../../data/db/ofw.csv"  # Replace with the actual path to your CSV file
json_file_path = "../../data/db/ofw.json"  # Replace with the desired output JSON file path

csv_data = []

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        csv_data.append(row)

# Write JSON data
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(csv_data, jsonfile, indent=2)

print("Conversion complete.")
