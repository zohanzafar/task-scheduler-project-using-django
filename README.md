# task-scheduler-project-using-django

# Task Manager API

This project is a Django-based **Task Manager API** that allows users to register, log in, create projects, and manage tasks within those projects. It supports full CRUD (Create, Read, Update, Delete) operations for tasks and utilizes Django's authentication system for user management. Sensitive configurations, such as the `SECRET_KEY`, are managed securely using environment variables.

## Getting Started

### Prerequisites

**Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **Django 5.1**: This project is built with Django version 5.1.
- **Virtual Environment**: It's recommended to use a virtual environment to manage your project's dependencies.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone 
   https://github.com/zohanzafar/task-scheduler-project-using-django.git
   cd task-scheduler-project-using-django
   ```

2. **Create and Activate a Virtual Environment**:

   - On **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up the Environment

1. **Create a `.env` File**:

   In the project's root directory, create a file named `.env`. This file will store your environment variables, including the `SECRET_KEY`.

2. **Generate a Secret Key**:

   ```
   SECRET_KEY=your_generated_secret_key
   ```

3. **Configure `settings.py`**:

   In your `settings.py` file, load the environment variables using `python-dotenv`:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  

   SECRET_KEY = os.getenv("SECRET_KEY")
   ```

   This approach ensures that your `SECRET_KEY` is securely loaded from the environment variable.

### Database Migrations

After setting up the environment, apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a Superuser

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### Running the Server

Start the development server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to access the application.