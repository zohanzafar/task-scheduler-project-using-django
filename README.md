# task-scheduler-project-using-django

summaryTask Manager APIhttps://github.com/your-username/task-manager-api

# Task Manager API

This project is a Django-based **Task Manager API** that allows users to register, log in, create projects, and manage tasks within those projects. It supports full CRUD (Create, Read, Update, Delete) operations for tasks and utilizes Django's authentication system for user management. Sensitive configurations, such as the `SECRET_KEY`, are managed securely using environment variables.

## Table of Contents

- [Task Manager API](#task-manager-api)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Setting Up the Environment](#setting-up-the-environment)
    - [Database Migrations](#database-migrations)
    - [Creating a Superuser](#creating-a-superuser)
    - [Running the Server](#running-the-server)
  - [Environment Variables and Secret Key](#environment-variables-and-secret-key)
    - [Generating a Secret Key](#generating-a-secret-key)
    - [Creating the `.env` File](#creating-the-env-file)
    - [Configuring `settings.py`](#configuring-settingspy)
  - [API Endpoints](#api-endpoints)
    - [User Authentication](#user-authentication)
    - [Project Management](#project-management)
    - [Task Management](#task-management)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

### Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **Django 5.1**: This project is built with Django version 5.1.
- **Virtual Environment**: It's recommended to use a virtual environment to manage your project's dependencies.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/zohanzafar/task-scheduler-project-using-django.git
   cd task-manager-api
   ```

2. **Create and Activate a Virtual Environment**:

   - On **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up the Environment

1. **Create a `.env` File**:

   In the project's root directory, create a file named `.env`. This file will store your environment variables, including the `SECRET_KEY`.

2. **Generate a Secret Key**:

   To generate a new secret key, you can use the following Python command:

   ```bash
    
   ```

   Copy the generated key and paste it into the `.env` file:

   ```
   SECRET_KEY=your_generated_secret_key
   ```

   *Note*: The `.env` file is excluded from version control (`.gitignore`) to protect your secret key.

3. **Configure `settings.py`**:

   In your `settings.py` file, load the environment variables using `python-dotenv`:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  # Load variables from .env

   SECRET_KEY = os.getenv("SECRET_KEY")
   ```

   This approach ensures that your `SECRET_KEY` is securely loaded from the environment variable.

### Database Migrations

After setting up the environment, apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a Superuser

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Running the Server

Start the development server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to access the application.

## API Endpoints

The Task Manager API provides the following endpoints:

### User Authentication

- **Register**: `/api/auth/register/` [POST]
- **Login**: `/api/auth/login/` [POST]
- **Logout**: `/api/auth/logout/` [POST]
- **Change Password**: `/api/auth/change-password/` [POST]

### Project Management

- **Create Project**: `/api/projects/` [POST]
- **List Projects**: `/api/projects/` [GET]
- **Retrieve Project**: `/api/projects/<project_id>/` [GET]
- **Update Project**: `/api/projects/<project_id>/` [PUT]
- **Delete Project**: `/api/projects/<project_id>/` [DELETE]

### Task Management

- **Create Task**: `/api/tasks/` [POST]
- **List Tasks**: `/api/tasks/` [GET]
- **Retrieve Task**: `/api/tasks/<task_id>/` [GET]
- **Update Task**: `/api/tasks/<task_id>/` [PUT]
- **Delete Task**: `/api/tasks/<task_id>/` [DELETE]

Ensure to include authentication tokens in the headers for protected endpoints.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note*: Remember to replace placeholders like `your-username` and `your_generated_secret_key` with your actual GitHub username and the generated secret key, respectively.

By following these instructions, you can set up, configure, and run the Task Manager API on your local machine.