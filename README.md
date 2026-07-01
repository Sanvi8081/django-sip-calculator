# SIP Calculator

A simple SIP (Systematic Investment Plan) Calculator built using Django. This project was created to understand the fundamentals of Django, including URL routing, views, templates, static files, and handling user input through forms.

## ✨ Features

- Calculate Total Investment
- Calculate Estimated Returns
- Calculate Total Wealth (Maturity Amount)
- Clean and responsive user interface
- Built using Django templates and CSS

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3

## Project Structure

```
django-sip-calculator/
│
├── calculator/
│   ├── templates/
│   │   └── home.html
│   ├── static/
│   │   └── calculator/
│   │       ├── css/
│   │       └── images/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## 🚀 How It Works

1. The user enters:
   - Monthly Investment
   - Expected Annual Return
   - Investment Duration
2. Django processes the form data in the view.
3. The SIP maturity amount is calculated using the standard SIP formula.
4. The calculated values are displayed on the webpage.

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd django-sip-calculator
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Learning Objectives

This project was built to practice:

- Django Project Structure
- URL Routing
- Views
- Django Templates
- Static Files


## 📸 Screenshots

### SIP Calculator


<img width="1502" height="756" alt="Screenshot 2026-07-01 121815" src="https://github.com/user-attachments/assets/9692fb47-9663-4835-a9b9-8a54aaa5448a" />

<img width="1388" height="848" alt="Screenshot 2026-07-01 121900" src="https://github.com/user-attachments/assets/ba1b812c-912d-434b-8c0b-7653693ecbfa" />

