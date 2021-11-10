# Quizes
### This is manual how to install this project locally

---
## 1. Make virtual environment & activate it

    python3 -m venv venv
    source venv/bin/activate

## Install requirements

    pip install --upgrade pip
    pip install -r requirements.txt

## 3. Make migrations

    python manage.py migrate
    
## 4. Create superuser

    python manage.py createsuperuser

## 5. Run server

    python manage.py runserver

