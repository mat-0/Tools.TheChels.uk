import pathlib
import requests
import yaml
import csv

# Define file paths
csv_file_path = pathlib.Path('NetflixViewingHistory.csv')
yaml_file_path = pathlib.Path('films.yml')
omdb_api_key = 'your_omdb_api_key'  # Replace with your actual OMDB API key

def read_film_titles_from_csv(csv_file_path):
    film_titles = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            film_titles.append(row[0])
    return film_titles

def write_film_titles_to_yaml(film_titles, yaml_file_path):
    with open(yaml_file_path, mode='w', encoding='utf-8') as yaml_file:
        yaml.dump({'films': film_titles}, yaml_file)

def fetch_film_details_from_omdb(film_titles, omdb_api_key):
    film_details = []
    for title in film_titles:
        response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}')
        if response.status_code == 200:
            film_details.append(response.json())
    return film_details

def write_film_details_to_yaml(film_details, yaml_file_path):
    with open(yaml_file_path, mode='w', encoding='utf-8') as yaml_file:
        yaml.dump({'films': film_details}, yaml_file)

if __name__ == '__main__':
    film_titles = read_film_titles_from_csv(csv_file_path)
    write_film_titles_to_yaml(film_titles, yaml_file_path)
    # film_details = fetch_film_details_from_omdb(film_titles, omdb_api_key)
    # write_film_details_to_yaml(film_details, yaml_file_path)
    print('Films data saved to YAML file.')