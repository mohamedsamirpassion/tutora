from app import create_app, db
from app.models.user import User
from app.models.course import Course
from werkzeug.security import generate_password_hash

def seed_database():
    """Add initial data to the database."""
    app = create_app()
    with app.app_context():
        # Create admin user
        admin = User(
            username="admin",
            email="admin@tutora.com",
            first_name="Admin",
            last_name="User",
            phone="123-456-7890",
            is_admin=True
        )
        admin.password_hash = generate_password_hash("admin123")
        
        # Create courses
        general_english = Course(
            title="General English - Beginner",
            description="A comprehensive course designed for beginners to build a strong foundation in English language skills including reading, writing, speaking, and listening.",
            category="General English",
            duration="8 weeks",
            price=199.99,
            is_active=True,
            image_url="/static/images/course-placeholder.jpg"
        )
        
        conversation = Course(
            title="Conversation Skills",
            description="Improve your speaking fluency and confidence through interactive conversation practice, role-plays, and discussions on various topics.",
            category="Conversation",
            duration="6 weeks",
            price=149.99,
            is_active=True,
            image_url="/static/images/course-placeholder.jpg"
        )
        
        phonetics = Course(
            title="Phonetics and Pronunciation",
            description="Master English pronunciation with a focus on phonetics, intonation, rhythm, and accent reduction techniques.",
            category="Phonetics",
            duration="4 weeks",
            price=129.99,
            is_active=True,
            image_url="/static/images/course-placeholder.jpg"
        )
        
        # Add to database
        db.session.add(admin)
        db.session.add(general_english)
        db.session.add(conversation)
        db.session.add(phonetics)
        
        # Commit changes
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database() 