from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
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


class nameEntry(FlaskForm):
    name = StringField('Product name', validators=[DataRequired()])
    minprice = IntegerField('Minimum Product price')
    maxprice = IntegerField('Maximum Product price')
    submit = SubmitField('Search')

class priceEntry(FlaskForm):
    k = StringField('Product name', validators=[DataRequired()])
    submit = SubmitField('Search')

@bp.route('/browse-products', methods=['GET', 'POST'])
def browseproducts():
    nameform = nameEntry()
    priceform = priceEntry()
    if nameform.validate_on_submit():
        print("working")
        products = ProductModel.get_by_feature(nameform.name.data,nameform.minprice.data, nameform.maxprice.data)
    else:
        print(1)    
        print(nameform.maxprice.data)
        products = None
    allproducts = ProductModel.get_all()
    # render the page by adding information to the oldCarts.html file
    return render_template('browse-products.html',
                            nameform=nameform,
                            priceform=priceform,
                            products=products,
                            allproducts=allproducts)