from flask import Blueprint, render_template
from ..models import Student, Transaction

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def index():
    total_students = Student.query.count()
    due_students = Student.query.filter(Student.fees_due > 0).count()
    total_income = sum(transaction.amount for transaction in Transaction.query.all())
    
    return render_template('dashboard.html', total_students=total_students,
                           due_students=due_students, total_income=total_income)
