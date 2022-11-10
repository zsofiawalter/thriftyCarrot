from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form
from wtforms.validators import DataRequired

from .models.cartModel import CartModel

from flask import Blueprint
bp = Blueprint('carts', __name__)

class newCartProducts(Form):
    product = StringField('Product', validators=[DataRequired()])

class newCartForm(FlaskForm):
    cartname = StringField('Cart Name', validators=[DataRequired()])
    products = FieldList(FormField(newCartProducts), min_entries=1)
    submit = SubmitField('Next')

@bp.route('/newcart', methods=['GET', 'POST'])
def newcart():
    form = newCartForm()
    cart = None

    return render_template('newCart.html',
                            cart = cart,
                            form = form)

# back end endpoint
@bp.route('/carts', methods=['GET', 'POST'])
def carts():
    form = userEntry()
    if form.validate_on_submit():
        cart = CartModel.get(form.uid.data)
    else:
        cart = None

    return render_template('carts.html',
                            cart = cart,
                            form = form)