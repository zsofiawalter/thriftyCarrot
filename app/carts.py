from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form
from wtforms.validators import DataRequired

from datetime import datetime

from .models.cartModel import CartModel, CartListModel

from flask import Blueprint
bp = Blueprint('carts', __name__)

# dynamic form adapted from: https://www.rmedgar.com/blog/dynamic-fields-flask-wtf/

class newCartProducts(Form):
    product = StringField('Product', validators=[DataRequired()])

class newCartForm(FlaskForm):
    cart_name = StringField('Cart Name', validators=[DataRequired()])
    products = FieldList(FormField(newCartProducts), min_entries=1, max_entries=50)
    submit = SubmitField('Next')

@bp.route('/newcart', methods=['GET', 'POST'])
@login_required
def newcart():
    form = newCartForm()
    template_form = newCartProducts(prefix='products-_-')

    if form.validate_on_submit():
        uid = current_user.id
        cart_name = form.cart_name.data
        time_started = datetime.now()
        CartModel.startCart(uid, cart_name, time_started)
        # add product names to cart list
        for product in form.products.data:
            # add product to cart list
            CartListModel.addToCartList(uid, product['product'])
        return redirect(url_for('carts.cartInProgress'))

    return render_template('newCart.html',
                            form = form,
                            _template = template_form)

@bp.route('/<cart_name>', methods=['GET', 'POST'])
@login_required
def cartInProgress(cart_name):
    return render_template('cartInProgress.html',
                            cart_name = cart_name)