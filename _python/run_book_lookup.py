

import yaml
import sys
import datetime
import os
import isbnlib


class Book:
    def __init__(self, isbn, date_finished, title, authors, published_date, description, industry_identifiers, page_count, print_type, categories, image_links, language, canonical_volume_link):
        self.isbn = isbn
        self.date_finished = date_finished
        self.title = title
        self.authors = authors
        self.published_date = published_date
        self.description = description
        self.industry_identifiers = industry_identifiers
        self.page_count = page_count
        self.print_type = print_type
        self.categories = categories
        self.image_links = image_links
        self.language = language
        self.canonical_volume_link = canonical_volume_link

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'date_finished': self.date_finished,
            'title': self.title,
            'authors': self.authors,
            'published_date': self.published_date,
            'industry_identifiers': self.industry_identifiers,
            'description': self.description,
            'page_count': self.page_count,
            'print_type': self.print_type,
            'categories': self.categories,
            'image_links': self.image_links,
            'language': self.language,
            'canonical_volume_link': self.canonical_volume_link
        }

    def __repr__(self):
        return f"Book(title={self.title}, authors={self.authors}, published_date={self.published_date})"


def booking(file_path, isbn, date=None):
    if date is None:
        date = datetime.datetime.now().isoformat()

    # check if isbn is valid
    if not isbnlib.is_isbn13(isbn):
        raise Exception('Invalid ISBN')

    try:
        datetime.datetime.fromisoformat(date)
    except ValueError:
        raise Exception('Invalid date')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
    else:
        data = []

    for book in data:
        if book['isbn'] == isbn:
            raise Exception('Book already exists')

    # get book data
    book_data = isbnlib.meta(isbn, service='goob')
    title = book_data['Title']
    authors = book_data['Authors'] if 'Authors' in book_data else []
    published_date = book_data['Year'] if 'Year' in book_data else None
    industry_identifiers = book_data['ISBN-13'] if 'ISBN-13' in book_data else None
    description = book_data['Description'] if 'Description' in book_data else None
    page_count = book_data['Number of Pages'] if 'Number of Pages' in book_data else None
    print_type = book_data['Type'] if 'Type' in book_data else None
    categories = book_data['Subjects'] if 'Subjects' in book_data else []
    image_links = book_data['Thumbnail'] if 'Thumbnail' in book_data else None
    language = book_data['Language'] if 'Language' in book_data else None
    canonical_volume_link = book_data['URL'] if 'URL' in book_data else None

    new_book = Book(
        isbn=isbn,
        date_finished=date,
        title=title,
        authors=authors,
        published_date=published_date,
        description=description,
        industry_identifiers=industry_identifiers,
        page_count=page_count,
        print_type=print_type,
        categories=categories,
        image_links=image_links,
        language=language,
        canonical_volume_link=canonical_volume_link
    )

    data.append(new_book.to_dict())

    with open(file_path, 'w') as file:
        yaml.dump(data, file)

    return new_book


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(booking(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 4:
        print(booking(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        print('Usage: python booking.py <file_path> <isbn> [date]')
        sys.exit(1)