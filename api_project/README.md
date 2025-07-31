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
