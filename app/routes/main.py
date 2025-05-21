from flask import Blueprint, render_template, current_app, flash, redirect, url_for, request
from app.models.course import Course
from app.models.message import Message
from app.forms.message_forms import ContactForm
from app import db

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

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent! We will get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html', title='Contact Us', form=form) 