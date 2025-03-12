from io import BytesIO
import pathlib
import requests
import os
import argparse
from datetime import date
from PIL import Image
from ruamel.yaml import YAML

OUTPUT_FILE = "books.yml"
yaml = YAML()
yaml.default_flow_style = False

def load_book_file(file_path):
    path = pathlib.Path(file_path)
    if not path.exists():
        return []
    with path.open("r") as f:
        data = yaml.load(f)
        return data if isinstance(data, list) else []

def save_books(file_path, books):
    with pathlib.Path(file_path).open("w") as f:
        yaml.dump(books, f)

def add_book_to_list(book_data):
    library_books = load_book_file(OUTPUT_FILE)
    isbn = book_data["isbn"]
    if isinstance(isbn, list):
        isbn = isbn[0]
    for book in library_books:
        if book["isbn"] == isbn:
            return False
    library_books.append(book_data)
    save_books(OUTPUT_FILE, library_books)
    return True

def download_book_cover(book_data):
    cover_url = book_data["cover"]
    cover_response = requests.get(cover_url)
    print(cover_response)
    isbn_key = book_data["isbn"]
    if isinstance(isbn_key, list):
        isbn_key = isbn_key[0]
        isbn_key = isbn_key.replace("-", "").replace(" ", "")
        new_cover_path = f"./image/books/book-{isbn_key}.png"
        os.makedirs(os.path.dirname(new_cover_path), exist_ok=True)
        img = Image.open(BytesIO(cover_response.content))
        img.save(new_cover_path, 'PNG')
        print(f"Cover image saved to {new_cover_path}")
    else:
        print(f"Failed to download cover image. Status code: {cover_response.status_code}")
    return True


def get_book_data(isbn):
    headers = {
        "Author": "MatB - ensemblist.uk@gmail.com",
    }
    url = f"https://openlibrary.org/isbn/{isbn}.yml"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = yaml.load(response.text)
    if not data:
        return None

    book_data = {
        "isbn": data["isbn_13"][0] if "isbn_13" in data else isbn,
        "dateFinished": date.today().isoformat(),
        "title": data["title"],
        "publisher": data["publishers"][0] if "publishers" in data else "",
        "cover": f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg",
        "notes": "",
    }
    return book_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a book to the library.")
    parser.add_argument("--isbn", required=True, help="The ISBN of the book.")

    args = parser.parse_args()

    saved_book = get_book_data(args.isbn)
    if saved_book:
        if add_book_to_list(saved_book):
            download_book_cover(saved_book)
            print("Book added successfully.")
        else:
            print("Book already exists in the list.")
    else:
        print("Book not found.")