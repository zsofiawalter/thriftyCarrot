from flask import render_template
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import datetime

from .models.product import Product
from .models.freshyCarrotModel import FreshyCarrotModel

from flask import Blueprint
bp = Blueprint('freshyCarrot', __name__)

class userEntry(FlaskForm):
    uid = StringField('UserID', validators=[DataRequired()])
    submit = SubmitField('Search For User Freshy Carrots')

# back end endpoint
@bp.route('/freshyCarrot', methods=['GET', 'POST'])
def freshyCarrot():
    form = userEntry()
    if form.validate_on_submit():
        recentFresh = FreshyCarrotModel.get_5_recent_fresh_by_uid(form.uid.data)
        recentRotten = FreshyCarrotModel.get_5_recent_rotten_by_uid(form.uid.data)
    else:
        recentFresh = None
        recentRotten = None
    # render the page by adding information to the freshyCarrots.html file
    return render_template('freshyCarrots.html',
                            form=form,
                            recentFresh=recentFresh,
                            recentRotten=recentRotten)