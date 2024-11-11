from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(20))
    shift_id = db.Column(db.Integer, db.ForeignKey('shift.id'))
    is_active = db.Column(db.Boolean, default=True)
    fees_due = db.Column(db.Float, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime)
    type = db.Column(db.String(10))  # "credit" or "debit"

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    seat_count = db.Column(db.Integer)
    # Additional attributes as needed
