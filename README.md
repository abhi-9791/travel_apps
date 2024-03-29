# travel_app
# By Wilson Wings
# Django Project

This is a Django project for managing destinations.
## Setup

1. Clone the repository:

git clone `https://github.com/abhi-9791/travel_apps`

2. Create a virtual environment and activate it

python -m venv `travel_env`
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

## Throttling

The project implements throttling to limit the number of requests. By default, users are limited to 500 requests per day.


## Test Descriptions

### Unit Tests

#### Destinations_Unit_Test


- `test_name_max_length`: Tests the maximum length constraint for the `name` field.
- `test_country_max_length`: Tests the maximum length constraint for the `country` field.

 `test_best_time_to_visit_max_length`: Tests the length value is grate or less`best_time_to_visit` field.
- `test_category_choices`: Tests that the `category` field only accepts valid choices.
- `test_image_url_max_length`: Tests the image value length constraint for the `image_url` field.

### Integration Tests

#### DestinationAPI_Integration

- `test_list_destinations`: Tests listing all destinations.
- `test_retrieve_destination`: Tests retrieving a single destination.
- `test_create_destination`: Tests creating a new destination.
- `test_update_destination`: Tests updating an existing destination.
- `test_delete_destination`: Tests deleting an existing destination.
- `test_unauthenticated_access`: Tests that endpoints require authentication.
- `test_invalid_destination_id`: Tests handling of requests with invalid destination IDs.
- `test_invalid_create_data`: Tests handling of requests to create a destination with invalid data.

## Tested in postaman and Using Python requests modeule
You can see that code in `requests.ipynb`
i am providing all requests and responses

## i did not do the partial updation

## i provided Postman collection also