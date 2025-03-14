import json
import yaml

# Define the file paths
json_file_path = '../_data/films.json'
yaml_file_path = '../_data/films.yml'

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Write the data to a YAML file
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

print(f"Converted {json_file_path} to {yaml_file_path}")