import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    data = []
    
    # Read CSV file and load data into a list of dictionaries
    with open(csv_file, 'r') as csv_data:
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            data.append(row)

    # Write data to a JSON file
    with open(json_file, 'w') as json_data:
        json.dump(data, json_data, indent=4)

# Example usage
csv_file = 'active_nodes_november_v1.csv'
json_file = 'output.json'
csv_to_json(csv_file, json_file)