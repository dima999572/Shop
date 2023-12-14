# USER_API_URL = "http://user-service-c:5001"
import os
if os.environ.get('FLASK_ENV') == 'development':
    USER_API_URL = "http://0.0.0.0:5001"
else:
    USER_API_URL = "http://user-service.user-app:5001"
# BOOK_API_URL = "http://book-service-c:5002"
if os.environ.get('FLASK_ENV') == 'development':
    BOOK_API_URL = "http://0.0.0.0:5002"
else:
    BOOK_API_URL = "http://book-service.book-app:5002"
# ORDER_API_URL = "http://order-service-c:5003"
if os.environ.get('FLASK_ENV') == 'development':
    ORDER_API_URL = "http://0.0.0.0:5003"
else:
    ORDER_API_URL = "http://order-service.order-app:5003"

