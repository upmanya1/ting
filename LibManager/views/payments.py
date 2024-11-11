from flask import Blueprint, render_template, redirect, url_for, request
from ..models import Transaction, Student
from ..forms import PaymentForm
from .. import db
from datetime import datetime

bp = Blueprint('payments', __name__, url_prefix='/payments')

@bp.route('/submit', methods=['GET', 'POST'])
def submit_payment():
    form = PaymentForm()
    if form.validate_on_submit():
        transaction = Transaction(student_id=form.student_id.data,
                                  amount=form.amount.data, date=datetime.now())
        db.session.add(transaction)
        student = Student.query.get(form.student_id.data)
        student.fees_due -= form.amount.data
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return render_template('submit_payment.html', form=form)
