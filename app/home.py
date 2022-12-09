from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
import datetime
import random
random.seed(0)

from .models.productModel import ProductModel
from .models.oldCartModel import OldCartModel
from .models.oldCartContentModel import OldCartContentModel
from .models.preferenceModel import PreferenceModel


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired

from flask import Blueprint
bp = Blueprint('home', __name__)

class userEntry(FlaskForm):
    uid = StringField('UserID', validators=[DataRequired()])
    submit = SubmitField('Search For Carts')

class reviewEntry(FlaskForm):
    like_dislike = BooleanField('Give a fresh carrot?')
    submit = SubmitField('AddReview')

@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    #TODO: *expansion* view cart in progress
    products = ProductModel.get_all(datetime.datetime(2022, 10, 1, 0, 0, 0))
    purchases = OldCartModel.get_all_by_uid_since(
        current_user.id, datetime.datetime(1980, 9, 14, 0, 0, 0))
    
    carts = OldCartModel.get_recent_three_by_uid(current_user.id)
    for cart in carts:
        cart.time_created = cart.time_created.strftime("%b %d, %Y")
    cartContent = OldCartContentModel.get_content_of_recent_three_by_uid(current_user.id)
    purchase_category = OldCartContentModel.get_count_by_category(current_user.id)
    last_cart_prices = OldCartContentModel.get_last_cart_prices(current_user.id)
    data = []
    data_length = 0 
    last_cart = []
    last_cart_length = 0
    for product in last_cart_prices:
        if last_cart_length == 0:
            last_cart.append(["Product name","Total price"])
        last_cart_length+=1
        if [product.product_name, float(product.price)] not in last_cart:
            last_cart.append([product.product_name, float(product.price)])
    for purchase in purchase_category:
        if data_length == 0:
            data.append(["Category","Total price"])
        data_length+=1
        data.append([purchase.category, float(purchase.price)])
    print(data)
    print(last_cart)

    for content in cartContent:
        content.review = PreferenceModel.get_product_review(current_user.id, content.pid)
        if(content.review): content.like_dislike = content.review[0].like_dislike
    count = data_length
    if request.method == 'POST':
        uid = current_user.id
        input = []
        if(request.form.get('fresh-carrot')):
            input = request.form.get('fresh-carrot').split("-")
        elif(request.form.get('rotten-carrot')):
            input = request.form.get('rotten-carrot').split("-")
        if len(input)>1:
            if input[0] == "delete":
                PreferenceModel.delete(uid, input[2])
            elif input[0] == "update":
                PreferenceModel.update(uid, input[2], (input[1]=="freshcarrot"))
            elif input[0] == "add":
                PreferenceModel.insert(uid, input[2], (input[1]=="freshcarrot"))
            return(redirect(url_for("home.home")))
        

    return render_template('home.html',
            current_user=current_user,
            avail_products=products,
            purchase_history=purchases,
            category_data = data,
            last_cart = last_cart,
            count = count,
            carts=carts,
            cartContent=cartContent)

