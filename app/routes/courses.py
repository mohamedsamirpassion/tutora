from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models.course import Course, CourseEnrollment

bp = Blueprint('courses', __name__)

@bp.route('/')
def index():
    courses = Course.query.filter_by(is_active=True).all()
    return render_template('courses/index.html', title='All Courses', courses=courses)

@bp.route('/<int:id>')
def detail(id):
    course = Course.query.get_or_404(id)
    return render_template('courses/detail.html', title=course.title, course=course)

@bp.route('/<int:id>/enroll', methods=['GET', 'POST'])
@login_required
def enroll(id):
    course = Course.query.get_or_404(id)
    
    # Check if user is already enrolled
    existing_enrollment = CourseEnrollment.query.filter_by(
        user_id=current_user.id, course_id=course.id
    ).first()
    
    if existing_enrollment:
        flash('You are already enrolled in this course.', 'info')
        return redirect(url_for('courses.detail', id=course.id))
    
    # Create new enrollment
    enrollment = CourseEnrollment(user_id=current_user.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()
    
    flash(f'You have successfully enrolled in {course.title}!', 'success')
    return redirect(url_for('courses.my_courses'))

@bp.route('/my-courses')
@login_required
def my_courses():
    enrollments = CourseEnrollment.query.filter_by(user_id=current_user.id).all()
    return render_template('courses/my_courses.html', 
                          title='My Courses',
                          enrollments=enrollments) 