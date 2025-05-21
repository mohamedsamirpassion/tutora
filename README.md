# Tutora - English Language Institute

Tutora is a web application for an English language teaching institute that offers online courses. The platform allows users to browse available courses, enroll in them, and book placement tests.

## Features

- **User Authentication**: Register, login, and manage user accounts
- **Course Management**: Browse, view, and enroll in courses
- **Booking System**: Book placement tests with preferred date and time
- **Admin Dashboard**: Manage courses and bookings, view statistics

## Tech Stack

- **Backend**: Python with Flask web framework
- **Database**: SQLAlchemy ORM (SQLite for development, PostgreSQL for production)
- **Frontend**: HTML/CSS/JavaScript with Bootstrap 5
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF and WTForms

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tutora
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables (optional):
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=your-database-url
   ```

6. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. Run the application:
   ```
   flask run
   ```

8. Access the application at `http://localhost:5000`

## Admin Account Setup

To create an admin account:

1. Register a normal user account through the registration form
2. Access the SQLite database (or your configured database):
   ```
   sqlite3 app.db
   ```
3. Update the user to have admin privileges:
   ```sql
   UPDATE user SET is_admin = 1 WHERE username = 'your_username';
   ```
4. Exit the database:
   ```
   .exit
   ```

## Folder Structure

```
tutora/
├── app/                    # Application package
│   ├── forms/              # WTForms definitions
│   ├── models/             # SQLAlchemy models
│   ├── routes/             # Route handlers
│   ├── static/             # Static files (CSS, JS, images)
│   └── templates/          # Jinja2 templates
├── migrations/             # Database migrations
├── .env                    # Environment variables (create this)
├── app.py                  # Application entry point
├── config.py               # Configuration settings
└── requirements.txt        # Project dependencies
```

## License

This project is licensed under the MIT License. 