import csv 
import json

csv_file = 'output_streamlines.csv'
json_file = 'output_streamlines.json'

data =[]

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(f"Converted{csv_file} to {json_file}")
