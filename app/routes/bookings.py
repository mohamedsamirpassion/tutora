from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from datetime import datetime
from app import db
from app.models.booking import Booking
from app.forms.booking_forms import BookingForm

bp = Blueprint('bookings', __name__)

@bp.route('/placement-test', methods=['GET', 'POST'])
@login_required
def book_placement_test():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(
            user_id=current_user.id,
            booking_date=form.booking_date.data,
            booking_time=form.booking_time.data,
            notes=form.notes.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Your placement test has been booked successfully! We will confirm your booking soon.', 'success')
        return redirect(url_for('bookings.my_bookings'))
    
    return render_template('bookings/book.html', title='Book Placement Test', form=form)

@bp.route('/my-bookings')
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.booking_date.desc()).all()
    return render_template('bookings/my_bookings.html', title='My Bookings', bookings=bookings)

@bp.route('/<int:id>/cancel', methods=['POST'])
@login_required
def cancel_booking(id):
    booking = Booking.query.get_or_404(id)
    
    # Check if the booking belongs to the current user
    if booking.user_id != current_user.id:
        flash('You do not have permission to cancel this booking.', 'danger')
        return redirect(url_for('bookings.my_bookings'))
    
    # Check if the booking can be cancelled (not already confirmed or completed)
    if booking.status in ['confirmed', 'completed']:
        flash('This booking cannot be cancelled.', 'danger')
        return redirect(url_for('bookings.my_bookings'))
    
    booking.status = 'cancelled'
    db.session.commit()
    flash('Your booking has been cancelled.', 'success')
    return redirect(url_for('bookings.my_bookings')) 