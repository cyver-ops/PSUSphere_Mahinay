# 🎓 PSUSphere

A modern Django web application for managing student organizations at Palawan State University.

---

## 📖 Overview

**PSUSphere** is a centralized Student Organization Management System designed to simplify the administration and monitoring of university organizations.

The system allows administrators to manage colleges, academic programs, students, organizations, and memberships through an intuitive dashboard with search, sorting, authentication, and pagination functionalities.

---

## ✨ Features

### 📊 Dashboard

- View overall system statistics
- Total number of students
- Students who joined this year
- Total organizations
- Total academic programs

### 🏛️ College Management

- View all colleges
- Search colleges instantly

### 📚 Program Management

- View all academic programs
- Search programs
- Sort programs by:
  - Program name
  - Associated college

### 👨‍🎓 Student Management

- View all registered students
- Search students by name

### 🎯 Organization Management

- View all organizations
- Search organizations
- Sort organizations by:
  - College
  - Organization name

### 👥 Organization Membership Management

- View organization members
- Search members by student name
- Sort members by:
  - Student name
  - Date joined

### 🔐 Authentication System

Supports multiple authentication methods:

- Username login
- Email login
- Google OAuth Login
- GitHub OAuth Login

### ⚙️ Admin Panel

- Full Django Admin integration
- Manage all system data efficiently

### 📄 Pagination

- Implemented across all list pages for improved user experience

---

## 🛠️ Tech Stack

| Technology | Version |
|------------|---------|
| Python | 3.12 |
| Django | 6.0.2 |
| Database | SQLite |
| django-allauth | 65.x |
| django-widget-tweaks | Latest |
| Faker | Latest |

---

## 📂 Project Structure

```text
PSUSphere/
│
├── projectsite/
│   ├── manage.py
│   ├── projectsite/
│   └── apps/
│
├── requirements.txt
├── README.md
└── venv/
```

---

## 🚀 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PSUSphere.git

cd PSUSphere
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Navigate to the Django Project

```bash
cd projectsite
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 Access the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Social Login Configuration

PSUSphere uses **django-allauth** for Google and GitHub authentication.

Add your OAuth credentials inside:

```text
projectsite/settings.py
```

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '<your-google-client-id>',
            'secret': '<your-google-client-secret>',
            'key': ''
        }
    },

    'github': {
        'APP': {
            'client_id': '<your-github-client-id>',
            'secret': '<your-github-client-secret>',
            'key': ''
        }
    }
}
```

---

## 🔗 OAuth Redirect URLs

### Google OAuth

Create credentials in Google Cloud Console.

Redirect URI:

```text
http://127.0.0.1:8000/accounts/google/login/callback/
```

### GitHub OAuth

Create an OAuth App in GitHub Developer Settings.

Callback URL:

```text
http://127.0.0.1:8000/accounts/github/login/callback/
```

---

## 📦 Dependencies

Install manually if necessary:

```bash
pip install Django
pip install django-allauth
pip install django-widget-tweaks
pip install Faker
```

Or simply:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Cyver Mahinay**

Student Developer • Palawan State University

---

## 📜 License

This project was developed for academic and educational purposes.
