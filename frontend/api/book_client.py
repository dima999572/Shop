import requests
from . import BOOK_API_URL


class BookClient():
    @staticmethod
    def get_all_books():
        url = BOOK_API_URL + '/api/book/all' 
        return requests.get(url).json()


    @staticmethod
    def book_details(slug):
        url = f'{BOOK_API_URL}/api/book/{slug}'

        response = requests.get(url)
 
        if response:
            details = response.json()
        return details