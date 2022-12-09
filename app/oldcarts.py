from flask import render_template, url_for, flash, request, redirect
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
import datetime

from .models.oldCartModel import OldCartModel
from .models.oldCartContentModel import OldCartContentModel
from .models.preferenceModel import PreferenceModel
from flask import Blueprint
bp = Blueprint('oldcarts', __name__)

class userEntry(FlaskForm):
    uid = StringField('UserID', validators=[DataRequired()])
    submit = SubmitField('Search For Carts')

class reviewEntry(FlaskForm):
    like_dislike = BooleanField('Give a fresh carrot?')
    submit = SubmitField('AddReview')
# back end endpoint
@login_required
@bp.route('/oldcarts', methods=['GET', 'POST'])
def oldcarts():
    form = userEntry()
    if  form.validate_on_submit():
        carts = OldCartModel.get_recent_three_by_uid(form.uid.data)
        cartContent = OldCartContentModel.get_most_recent_by_uid(form.uid.data)
    else:
        carts = None
        cartContent = None
    # find all old cart purchases:
    if current_user.is_authenticated:
        currentUserCarts = OldCartModel.get_all_by_uid(
            current_user.id)

        currentUserCartContent = OldCartContentModel.get_all_oldcartcontent_by_uid(
            current_user.id)
    else:
        purchases = None
    data = []
    data_length = 0 
    purchase_category = OldCartContentModel.get_count_by_category(current_user.id)
    for purchase in purchase_category:
        if data_length == 0:
            data.append(["Category","Total price"])
        data_length+=1
        data.append([purchase.category, float(purchase.price)])
    for content in currentUserCartContent:
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
            return(redirect(url_for("oldcarts.oldcarts")))
        

    # render the page by adding information to the oldCarts.html file
    return render_template('oldCarts.html',
                            form=form,
                            carts=carts,
                            cartContent=cartContent,
                            currentUserCarts=currentUserCarts,
                            currentUserCartContent=currentUserCartContent)