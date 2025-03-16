import json
import yaml
import config

# Define the file paths

json_file_path = config.FILM_JSON
yaml_file_path = config.FILM_OUT

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Write the data to a YAML file
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

print(f"Converted {json_file_path} to {yaml_file_path}")