# 🎓 PSUSphere

A Django-based Student Organization Management System for Palawan State University that helps manage colleges, programs, students, organizations, and memberships in one centralized platform.

## ✨ Features

* 📊 Dashboard with system statistics
* 🏛️ Manage colleges and programs
* 👨‍🎓 Manage students
* 🎯 Manage organizations and members
* 🔍 Search and sort data
* 🔐 Authentication with Google and GitHub login
* ⚙️ Django Admin integration
* 📄 Pagination across pages

## 🛠️ Tech Stack

* Python 3.12
* Django 6.0.2
* SQLite
* django-allauth
* django-widget-tweaks
* Faker

## 🚀 Run Locally

```bash
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Navigate to project folder
cd projectsite

# Apply migrations
python manage.py migrate

# Create admin account (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔑 Social Login

Configure your Google and GitHub OAuth credentials inside:

```text
projectsite/settings.py
```

## 👨‍💻 Author

**Cyver Mahinay**

Developed for academic and educational purposes.
