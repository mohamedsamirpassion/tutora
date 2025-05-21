from flask import Blueprint, render_template, current_app
from app.models.course import Course

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    # Get featured courses (3 active courses)
    try:
        featured_courses = Course.query.filter_by(is_active=True).limit(3).all()
    except Exception:
        featured_courses = []
        
    return render_template('main/index.html', 
                          title='Tutora - English Language Institute',
                          featured_courses=featured_courses)

@bp.route('/about')
def about():
    return render_template('main/about.html', title='About Tutora')

@bp.route('/programs')
def programs():
    try:
        # Get all active courses grouped by category
        general_english = Course.query.filter_by(category='General English', is_active=True).all()
        conversation = Course.query.filter_by(category='Conversation', is_active=True).all()
        phonetics = Course.query.filter_by(category='Phonetics', is_active=True).all()
    except Exception:
        general_english = []
        conversation = []
        phonetics = []
    
    return render_template('main/programs.html', 
                          title='Our Programs',
                          general_english=general_english,
                          conversation=conversation,
                          phonetics=phonetics)

@bp.route('/contact')
def contact():
    return render_template('main/contact.html', title='Contact Us') 