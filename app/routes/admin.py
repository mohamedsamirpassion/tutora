from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from app import db
from app.models.user import User
from app.models.course import Course
from app.models.booking import Booking
from app.models.message import Message
from app.forms.course_forms import CourseForm
from app.forms.booking_forms import AdminBookingForm

bp = Blueprint('admin', __name__)

def admin_required(func):
    """Decorator to check if the current user is an admin"""
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    decorated_function.__name__ = func.__name__
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def index():
    # Count of users, courses, pending bookings, unread messages
    user_count = User.query.count()
    course_count = Course.query.count()
    pending_bookings = Booking.query.filter_by(status='pending').count()
    unread_messages = Message.query.filter_by(read=False).count()
    
    return render_template('admin/index.html', 
                          title='Admin Dashboard',
                          user_count=user_count,
                          course_count=course_count,
                          pending_bookings=pending_bookings,
                          unread_messages=unread_messages)

# Course Management
@bp.route('/courses')
@login_required
@admin_required
def courses():
    courses = Course.query.all()
    return render_template('admin/courses/index.html', title='Manage Courses', courses=courses)

@bp.route('/courses/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            title=form.title.data,
            description=form.description.data,
            category=form.category.data,
            duration=form.duration.data,
            price=form.price.data,
            is_active=form.is_active.data
        )
        
        # Handle image upload
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            # Create uploads directory if it doesn't exist
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.image.data.save(file_path)
            course.image_url = f'/static/uploads/{filename}'
        
        db.session.add(course)
        db.session.commit()
        flash('Course has been created successfully!', 'success')
        return redirect(url_for('admin.courses'))
    
    return render_template('admin/courses/form.html', title='New Course', form=form)

@bp.route('/courses/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_course(id):
    course = Course.query.get_or_404(id)
    form = CourseForm(obj=course)
    
    if form.validate_on_submit():
        course.title = form.title.data
        course.description = form.description.data
        course.category = form.category.data
        course.duration = form.duration.data
        course.price = form.price.data
        course.is_active = form.is_active.data
        
        # Handle image upload
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.image.data.save(file_path)
            course.image_url = f'/static/uploads/{filename}'
        
        db.session.commit()
        flash('Course has been updated successfully!', 'success')
        return redirect(url_for('admin.courses'))
    
    return render_template('admin/courses/form.html', title='Edit Course', form=form, course=course)

@bp.route('/courses/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('Course has been deleted.', 'success')
    return redirect(url_for('admin.courses'))

# Booking Management
@bp.route('/bookings')
@login_required
@admin_required
def bookings():
    bookings = Booking.query.order_by(Booking.booking_date.desc()).all()
    return render_template('admin/bookings/index.html', title='Manage Bookings', bookings=bookings)

@bp.route('/bookings/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_booking(id):
    booking = Booking.query.get_or_404(id)
    form = AdminBookingForm(obj=booking)
    
    if form.validate_on_submit():
        booking.status = form.status.data
        booking.notes = form.notes.data
        booking.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Booking has been updated successfully!', 'success')
        return redirect(url_for('admin.bookings'))
    
    # Get the user information for this booking
    user = User.query.get(booking.user_id)
    
    return render_template('admin/bookings/edit.html', 
                          title='Edit Booking', 
                          form=form, 
                          booking=booking,
                          user=user)

@bp.route('/messages')
@login_required
@admin_required
def messages():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return render_template('admin/messages/index.html', 
                          title='Contact Messages',
                          messages=messages)

@bp.route('/messages/<int:id>')
@login_required
@admin_required
def view_message(id):
    message = Message.query.get_or_404(id)
    
    # Mark as read if it wasn't already
    if not message.read:
        message.read = True
        db.session.commit()
        
    return render_template('admin/messages/view.html', 
                          title='View Message',
                          message=message)

@bp.route('/messages/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    flash('Message has been deleted.', 'success')
    return redirect(url_for('admin.messages')) 