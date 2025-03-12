import yaml
from collections import Counter

# Load the YAML file
with open('/Users/mat/Documents/GitHub/TheChels.uk/_data/films.yml', 'r') as file:
    films = yaml.safe_load(file)

# Extract the Imdb IDs
imdb_ids = [film['Imdb'] for film in films]

# Count the occurrences of each Imdb ID
imdb_counts = Counter(imdb_ids)

# Find duplicates
duplicates = {imdb: count for imdb, count in imdb_counts.items() if count > 1}

# Print duplicates
if duplicates:
    print("Duplicate entries found:")
    for imdb, count in duplicates.items():
        print(f"{imdb}: {count} times")
else:
    print("No duplicate entries found.")


