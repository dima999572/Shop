# Shop

## How Run the App Locally

1. Navigate to the 'user/', 'book/', 'order/', and 'frontend/' directories:

```bash
  $ cd user/
```

Repeat this step for each of the directories.

2. Create and activate a virtual environment:

```bash
  $ python3 -m venv .venv
  $ source .venv/bin/activate
```

3. Install the required dependencies:

```bash
  $ pip install -r requirements.txt
```

4. Set the '$FLASK_ENV' environment variable:

```bash
  $ export FLASK_ENV='development'
```

5. Create a 'database' directory:

```bash
  $ mkdir database
```

6. Initialize and set up the database by running the following commands inside each directory:

```bash
  $ flask db init
  $ flask db migrate
  $ flask db upgrade
```

7. Run all microservices

```bash
  $ python3 app.py
```

###

## Done!

Now you can connect to "http://0.0.0.0:5000" and have some fun with the web page.

P.S. You can add book entities using Postman or code.
