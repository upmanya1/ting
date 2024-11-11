from flask import Blueprint, render_template, redirect, url_for, request
from ..models import Student
from ..forms import StudentForm
from .. import db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students=students)

@bp.route('/new', methods=['GET', 'POST'])
def new_student():
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(name=form.name.data, contact=form.contact.data,
                              shift_id=form.shift_id.data, fees_due=form.fees_due.data)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('students.student_list'))
    return render_template('new_student.html', form=form)
