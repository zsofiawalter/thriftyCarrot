from flask import render_template
from flask_login import current_user, login_required
import datetime

from .models.productModel import ProductModel
from .models.oldCartModel import OldCartModel

from flask import Blueprint
bp = Blueprint('home', __name__)


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    #TODO: new cart button
    #TODO: *expansion* view cart in progress
    #TODO: cart history instead of products/purchase history
    products = ProductModel.get_all(datetime.datetime(2022, 10, 1, 0, 0, 0))
    purchases = OldCartModel.get_all_by_uid_since(
        current_user.id, datetime.datetime(1980, 9, 14, 0, 0, 0))
    return render_template('home.html',
            avail_products=products,
            purchase_history=purchases)
