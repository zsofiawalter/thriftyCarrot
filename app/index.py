from flask import render_template
from flask_login import current_user
import datetime

from .models.productModel import ProductModel
from .models.oldCartModel import OldCartModel

from flask import Blueprint
bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    # get all available products for sale:
    products = ProductModel.get_all(datetime.datetime(2022, 10, 1, 0, 0, 0))
    # find the products current user has bought:
    if current_user.is_authenticated:
        purchases = OldCartModel.get_all_by_uid_since(
            current_user.id, datetime.datetime(1980, 9, 14, 0, 0, 0))
    else:
        purchases = None
    # render the page by adding information to the index.html file
    return render_template('index.html',
                           avail_products=products,
                           purchase_history=purchases)
