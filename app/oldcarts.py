from flask import render_template
from flask_login import current_user
import datetime

from .models.oldCart import OldCart
from .models.oldCartContents import OldCartContent

from flask import Blueprint
bp = Blueprint('oldcarts', __name__)

@bp.route('/oldcarts')
def oldcarts():
    # find all old cart purchases:
    if current_user.is_authenticated:
        purchases = OldCartContent.get_all_by_uid_since(
            current_user.id, datetime.datetime(2018, 9, 14, 0, 0, 0))
    else:
        purchases = None
    # render the page by adding information to the oldCarts.html file
    return render_template('oldCarts.html',
                           purhcases=purchases)