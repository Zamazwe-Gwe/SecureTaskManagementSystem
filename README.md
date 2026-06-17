# Secure Task Management System

## Overview
Secure Task Management System is a web-based Django application developed to provide secure task management with user authentication, role-based access control, audit logging, and administrative management.

## Features

- User registration and login
- Profile page
- Create tasks
- Update tasks
- Delete tasks
- Task status management
- Django admin panel
- Audit logging
- Secure authentication

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap

## Project Structure

```
SecureTaskManagementSystem
│
├── accounts
├── auditlog
├── freeze
├── secure_task_app
├── tasks
├── manage.py
├── requirements.txt
└── .gitignore
```

## Dependencies

- Django
- django-admin-interface
- colorfield

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python manage.py migrate
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

## Main Functionalities

### Authentication

- User registration
- User login
- User logout

### Task Management

- Create tasks
- Edit tasks
- Delete tasks
- Task status tracking

### Audit Logs

The system records:

- Login activities
- Logout activities
- Task creation
- Task deletion

### Admin Panel

Accessible via:

```
http://127.0.0.1:8000/admin/
```

---

Developed using Django framework.

### Project Contributors

This project was collaboratively developed by:
- Zamazwe Oyintando Gwe
- Farah Fatini Binti Hazlin Shah
