# Task Manager

A simple Django web app where each user can manage their own to-do list.

## Features
- User registration and login
- Each user sees only their own tasks
- Add, delete, and mark tasks as completed
- Responsive design

## Setup

```bash
# Clone the project
git clone <your-repo-url>
cd taskmanager

# Install dependencies
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/users/` in your browser.

## Project Structure

```
taskmanager/
    users/          # handles registration, login, logout
    tasksapp/       # handles task creation, deletion, completion
```

## Usage
1. Register an account
2. Login
3. Add tasks using the form
4. Mark tasks as completed or delete them
5. Logout when done

## Tech Stack
- Python 3
- Django 6
- SQLite (default database)
- HTML / CSS
