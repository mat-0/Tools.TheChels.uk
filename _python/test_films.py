import pytest
import pathlib
import requests
import yaml
from run_film_lookup import get_film_data, load_films, save_films, add_film_to_list, add_film
from unittest.mock import patch

def test_get_film_data():
    mock_response = """
    <a href="/title/tt1234567/?ref_=fn_al_tt_1" >Test Film</a> (2025)
    """
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_response
        result = get_film_data("Test Film")
        assert result == [("tt1234567", "Test Film", "2025")]

def test_get_film_data_not_found():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        result = get_film_data("Test Film")
        assert result == []

def test_load_films(tmp_path):
    mock_yaml_data = [{"Imdb": "tt7654321", "Title": "Another Film", "Year": "2024", "Rating": "8"}]
    file_path = tmp_path / "films.yml"
    file_path.write_text(yaml.dump(mock_yaml_data))
    films = load_films(file_path)
    assert films == mock_yaml_data

def test_save_films(tmp_path):
    films = [{"Imdb": "tt7654321", "Title": "Another Film", "Year": "2024", "Rating": "8"}]
    file_path = tmp_path / "films.yml"
    save_films(file_path, films)
    written_data = yaml.safe_load(file_path.read_text())
    assert written_data == films

def test_add_film_to_list():
    films = [{"Imdb": "tt7654321", "Title": "Another Film", "Year": "2024", "Rating": "8"}]
    film_data = ("tt1234567", "Test Film", "2025")
    rating = "9"
    result = add_film_to_list(films, film_data, rating)
    assert result is True
    assert {"Imdb": "tt1234567", "Title": "Test Film", "Year": "2025", "Rating": "9"} in films


if __name__ == "__main__":
    pytest.main()