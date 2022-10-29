from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from .models.productModel import ProductModel

from flask import Blueprint
bp = Blueprint('products', __name__)

class userEntry(FlaskForm):
    k = StringField('Number of Products', validators=[DataRequired()])
    submit = SubmitField('Search')

# back end endpoint
@bp.route('/products', methods=['GET', 'POST'])
def products():
    form = userEntry()
    if form.validate_on_submit():
        products = ProductModel.getKMostExpensive(form.k.data)
    else:
        products = None
    # render the page by adding information to the oldCarts.html file
    return render_template('products.html',
                            form=form,
                            products=products)