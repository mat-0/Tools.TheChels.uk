import pytest
import datetime
import os
import yaml
from booking import booking, Book

TEST_FILE_PATH = '_python/test.yml'
ISBN = "9781732265189"

class Test_booking:
    def setup_method(self):
        # Ensure the test file is empty before each test
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def test_booking_valid_isbn_and_date(self):
        date = "2025-02-17T10:00:00"
        result = booking(TEST_FILE_PATH, ISBN, date)
        assert result.date_finished == date
        assert result.title is not None
        assert result.authors is not None

    def test_booking_valid_isbn_without_date(self):
        result = booking(TEST_FILE_PATH, ISBN)
        assert result.date_finished is not None
        assert result.title is not None
        assert result.authors is not None

    def test_booking_invalid_isbn(self):
        isbn_invalid = "invalid-isbn"
        date = "2025-02-17T10:00:00"
        with pytest.raises(Exception):
            booking(TEST_FILE_PATH, isbn_invalid, date)

    def test_booking_invalid_date(self):
        date = "invalid-date"
        with pytest.raises(Exception):
            booking(TEST_FILE_PATH, ISBN, date)

    def test_booking_missing_isbn(self):
        with pytest.raises(TypeError):
            booking(TEST_FILE_PATH)

    def test_booking_empty_isbn(self):
        isbn_empty = ""
        date = "2025-02-17T10:00:00"
        with pytest.raises(Exception):
            booking(TEST_FILE_PATH, isbn_empty, date)

    def test_booking_empty_date(self):
        date = ""
        with pytest.raises(Exception):
            booking(TEST_FILE_PATH, ISBN, date)

    def test_booking_output_format(self):
        date = "2025-02-17T10:00:00"
        result = booking(TEST_FILE_PATH, ISBN, date)
        assert isinstance(result.to_dict(), dict)
        assert 'date_finished' in result.to_dict()
        assert 'title' in result.to_dict()
        assert 'authors' in result.to_dict()

if __name__ == "__main__":
    pytest.main()