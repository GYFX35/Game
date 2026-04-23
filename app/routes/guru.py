from flask import Blueprint, render_template, jsonify
from flask_login import login_required

guru = Blueprint('guru', __name__)

# Mock product catalog
PRODUCTS = [
    {"id": 1, "name": "Golden Box Skin", "price": 100, "color": "gold"},
    {"id": 2, "name": "Emerald Box Skin", "price": 250, "color": "emerald"},
    {"id": 3, "name": "Ruby Box Skin", "price": 500, "color": "red"}
]

@guru.route('/shop')
@login_required
def shop_index():
    return render_template('shop.html', products=PRODUCTS)

@guru.route('/api/products')
def get_products():
    return jsonify(PRODUCTS)
