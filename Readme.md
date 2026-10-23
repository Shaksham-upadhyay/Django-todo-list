# Django Todo List

A task management web application built using Python and Django that helps users organize and manage their daily tasks.

## Features

- Create and manage tasks
- View all tasks in your todo list
- Update task details
- Delete tasks
- **Search tasks** by keyword
- **Sort tasks** to organize them efficiently
- Database integration using SQLite
- User authentication (only if implemented)

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Shaksham-upadhyay/Django-todo-list.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django-todo-list
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   ```

   Windows:

   ```bash
   myenv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser at `http://127.0.0.1:8000/`.

## Project Structure

```text
Django-todo-list/
├── todo/
├── todolist/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Learning Outcomes

- Understanding Django project structure
- Working with Django models and views
- Database operations using SQLite
- Building web applications with Python and Django

## Author

**Shaksham Upadhyay**

GitHub: [Shaksham-upadhyay](https://github.com/Shaksham-upadhyay)
