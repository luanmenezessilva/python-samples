import os
import json
import pandas as pd
from pathlib import Path

def json_to_csv(directory_path, output_file):
    # List to store all JSON data
    all_data = []
    
    # Get all JSON files in directory
    json_files = Path(directory_path).glob('*.json')
    
    # Read each JSON file
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # If data is a single dict, convert to list
            if isinstance(data, dict):
                data = [data]
            all_data.extend(data)
    
    # Convert to DataFrame and save as CSV
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv(output_file, index=False)
        print(f"CSV file created successfully: {output_file}")
    else:
        print("No JSON files found or all files were empty")

# Example usage
input_directory = "./data/ceps_searched"
formatted_file = "./data/ceps_formatted.csv"
json_to_csv(input_directory, formatted_file)