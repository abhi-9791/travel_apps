# travel_app
# By Wilson Wings
# Django Project

This is a Django project for managing destinations.
## Setup

1. Clone the repository:

git clone https://github.com/abhi-9791/travel_apps

2. Create a virtual environment and activate it

python -m venv travel_env
venv\Scripts\activate


2.Install dependencies:
pip install -r requirements.txt

3.Apply migrations:
python manage.py migrate

4.Create a superuser (optional):
python manage.py createsuperuser

5.Running the Project
To run the development server, use the following command:

python manage.py runserver
The server will start at http://localhost:8000/.

6.Running Tests
To run tests, use the following command:
python manage.py test

API Endpoints

/travel/destinations/: List and create destinations.
/travel/destinations/<id>/: Retrieve, update, and delete a specific destination.
Authentication
This project uses token-based authentication. To obtain a token, you can use the /travel/token/ endpoint with your username and password.

For example:

curl -X POST -d "username=<your_username>&password=<your_password>" http://localhost:8000/travel/token/

Throttling
The project implements throttling to limit the number of requests. By default, users are limited to 500 requests per day.
