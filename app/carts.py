from flask import render_template
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import datetime

from .models.product import Product
from .models.oldCartModel import OldCartModel
from .models.oldCartContentsModel import OldCartContentModel
from .models.carts import Cart

from flask import Blueprint
bp = Blueprint('carts', __name__)

class userEntry(FlaskForm):
    uid = StringField('UserID', validators=[DataRequired()])
    submit = SubmitField('View current cart')

# back end endpoint
@bp.route('/carts', methods=['GET', 'POST'])
def carts():
    form = userEntry()
    if form.validate_on_submit():
        cart = Cart.get(form.uid.data)
    else:
        cart = None

    return render_template('carts.html',
                            cart = cart,
                            form = form)
