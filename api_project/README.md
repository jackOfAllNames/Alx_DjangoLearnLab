# Django REST API for Book Management

A beginner-friendly Django REST Framework project for managing books with user registration, authentication, and CRUD operations. This project demonstrates how to build a simple API with token-based authentication.

## Features

- User registration and login with token authentication
- List all books (public endpoint)
- Full CRUD for books (authenticated users only)
- Clean, modular code using Django REST Framework best practices

## Project Structure
```
api_project/ 
├── api/ 
│ ├── __init.py__ 
│ ├── admin.py 
│ ├── apps.py 
│ ├── models.py 
│ ├── serializers.py 
│ ├── tests.py 
│ ├── urls.py 
│ └── views.py 
├── api_project/ 
│ ├── __init.py__ 
│ ├── asgi.py
│ ├── settings.py 
│ ├── urls.py 
│ └── wsgi.py 
├── .gitignore 
├── db.sqlite3 
├── manage.py 
└── README.md
```

## Setup & Installation

1. **Clone the repository**  
```shell
git clone git@github.com:jackOfAllNames/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/api_project
```

2. **Create and activate a virtual environment**  
```shell
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**  
```shell
pip install django
pip install django djangorestframework
```

4. **Apply migrations**  
```shell
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**  
```shell
python manage.py createsuperuser
```

6. **Run the development server**  
```shell
python manage.py runserver
```


## API Endpoints
|Endpoint|Method|Description|Auth Required|
|---|---|---|---|
|/api/register/|POST|Register a new user|No|
|/api/login/|POST|Obtain authentication token|No|
|/api/books/|GET|List all books|No|
|/api/books/|POST|Create a new book|Yes|
|/api/books/<id>/|GET|Retrieve a book by ID|Yes|
|/api/books/<id>/|PUT|Update a book by ID|Yes|
|/api/books/<id>/|DELETE|Delete a book by ID|Yes|


## Authentication Flow
### 1. Register a New User

**Endpoint:** POST /api/register/

**Body:**

```shell
{
    "username": "yourusername",
    "email": "email@example.com",
    "password": "securepassword123"
}
```
**Response:**

```shell
{
    "username": "yourusername",
    "email": "email@example.com"
}
```

### 2. Obtain an Authentication Token

**Endpoint:** POST /api/login/

**Body:**
```shell
{
    "username": "yourusername",
    "password": "securePassword123"
}
```
**Response:**

```shell
{
    "token": <your-token>
}
```

### 3. Make Authenticated Requests
Include the token in the Authorization header for endpoints that require authentication:
```Authorization
Token <your-token>
```

## Key Dependencies
- Django
- Django REST Framework
- Token Authentication

## Developer Notes
- All API logic is in `api/views.py`.
- User registration uses a custom serializer (`RegisterSerializer`).
- Token authentication is handled by `CustomAuthToken`.
- Book CRUD is managed by `BookViewSet` and `BookList`.
- Update `api/urls.py` and `api_project/urls.py` to route endpoints as needed.
- For testing, use tools like Postman or curl.
