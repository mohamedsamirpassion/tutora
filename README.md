# Tutora - English Language Institute

Tutora is a comprehensive web application for an English language teaching institute that offers online and in-person courses. The platform allows users to browse available courses, enroll in them, book placement tests, and manage their learning journey.

## 📝 Project Overview

**Repository Link**: [https://github.com/mohamedsamirpassion/tutora.git](https://github.com/mohamedsamirpassion/tutora.git)

Tutora aims to streamline the process of connecting students with quality English language education. The platform provides:

- User-friendly interface for course browsing and enrollment
- Secure authentication system for students and administrators
- Comprehensive admin dashboard for course and student management
- Responsive design that works across all devices

## ✨ Features

### For Students
- **Account Management**: Register, login, and manage personal profiles
- **Course Catalog**: Browse and search available courses with details and pricing
- **Enrollment**: Enroll in courses and track learning progress
- **Booking System**: Schedule placement tests with preferred date and time
- **Learning Dashboard**: View enrolled courses and upcoming sessions

### For Administrators
- **Admin Dashboard**: Get an overview of site statistics, recent activities, and key metrics
- **Course Management**: Create, edit, and delete courses, set pricing and availability
- **Booking Administration**: View, approve, and manage student bookings
- **User Management**: Manage student accounts and access privileges
- **Content Management**: Update site content and course materials

## 🛠️ Tech Stack

### Backend
- **Python 3.x**: Core programming language
- **Flask**: Web application framework
- **SQLAlchemy**: ORM for database interaction
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and validation

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Bootstrap 5**: Responsive design framework
- **JavaScript**: Client-side interactivity
- **Jinja2**: Templating engine

### Database
- **SQLite**: Development database
- **PostgreSQL**: Production database (recommended for deployment)

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mohamedsamirpassion/tutora.git
   cd tutora
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables (optional):
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=your-database-url
   ```

6. Initialize the database:
   ```bash
   flask db upgrade
   ```

7. (Optional) Seed the database with sample data:
   ```bash
   python seed_data.py
   ```

8. Run the application:
   ```bash
   python run.py
   ```

9. Access the application at `http://localhost:5000`

## 👑 Admin Account Setup

To create an admin account:

1. Register a normal user account through the registration form
2. Access the SQLite database (or your configured database):
   ```bash
   sqlite3 app.db
   ```
3. Update the user to have admin privileges:
   ```sql
   UPDATE user SET is_administrator = 1 WHERE username = 'your_username';
   ```
4. Exit the database:
   ```
   .exit
   ```

## 📂 Folder Structure

```
tutora/
├── app/                    # Application package
│   ├── forms/              # WTForms definitions
│   │   ├── auth_forms.py   # Authentication forms
│   │   ├── booking_forms.py # Booking forms
│   │   └── course_forms.py # Course forms
│   ├── models/             # SQLAlchemy models
│   │   ├── booking.py      # Booking model
│   │   ├── course.py       # Course model
│   │   └── user.py         # User model
│   ├── routes/             # Route handlers
│   │   ├── admin.py        # Admin routes
│   │   ├── auth.py         # Authentication routes
│   │   ├── bookings.py     # Booking routes
│   │   ├── courses.py      # Course routes
│   │   └── main.py         # Main site routes
│   ├── static/             # Static files
│   │   ├── css/            # CSS files
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Image files
│   └── templates/          # Jinja2 templates
│       ├── admin/          # Admin templates
│       ├── auth/           # Authentication templates
│       ├── bookings/       # Booking templates
│       ├── courses/        # Course templates
│       └── main/           # Main site templates
├── migrations/             # Database migrations
├── app.py                  # Application configuration
├── config.py               # Configuration settings
├── run.py                  # Application entry point
├── seed_data.py            # Data seeding script
└── requirements.txt        # Project dependencies
```

## 🔄 Development Workflow

1. Create a new branch for each feature or bug fix
2. Make changes and test thoroughly
3. Commit changes with descriptive messages
4. Push changes to the remote repository
5. Create a pull request for review

## 🚢 Deployment

### Heroku Deployment
1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku CLI: `heroku login`
3. Create a new Heroku app: `heroku create tutora-app`
4. Add PostgreSQL addon: `heroku addons:create heroku-postgresql:hobby-dev`
5. Set environment variables: `heroku config:set SECRET_KEY=your-secret-key`
6. Push to Heroku: `git push heroku main`
7. Run migrations: `heroku run flask db upgrade`

### Other Platforms
The application can be deployed on any platform that supports Python applications, such as:
- AWS Elastic Beanstalk
- DigitalOcean App Platform
- Render
- PythonAnywhere

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact

For any questions or inquiries about the project, please contact:
- Email: tutoracommunity1@gmail.com 