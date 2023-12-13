import requests
from . import BOOK_API_URL


class BookClient():
    @staticmethod
    def get_all_books():
        url = f'{BOOK_API_URL}/api/book/all'
        response = requests.get(url)

        if response:
            books = response.json()
        return books


    @staticmethod
    def book_details(slug):
        url = f'{BOOK_API_URL}/api/book/{slug}'
        response = requests.get(url)
 
        if response:
            details = response.json()
        return details
