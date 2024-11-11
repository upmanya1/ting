from flask import Blueprint, send_file
import pandas as pd
from ..models import Student, Transaction

bp = Blueprint('export', __name__, url_prefix='/export')

@bp.route('/students')
def export_students():
    students = Student.query.all()
    df = pd.DataFrame([(s.id, s.name, s.contact, s.fees_due) for s in students],
                      columns=['ID', 'Name', 'Contact', 'Fees Due'])
    df.to_csv('students.csv', index=False)
    return send_file('students.csv', as_attachment=True)
