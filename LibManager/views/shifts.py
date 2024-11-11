from flask import Blueprint, render_template
from ..models import Shift

bp = Blueprint('shifts', __name__, url_prefix='/shifts')

@bp.route('/seat_map')
def seat_map():
    shifts = Shift.query.all()
    # Logic to calculate seat occupancy for each shift
    return render_template('seat_map.html', shifts=shifts)
