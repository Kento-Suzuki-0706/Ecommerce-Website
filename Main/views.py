from unicodedata import category
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Product, Order
from .forms import CheckoutForm
from . import db
from sqlalchemy import or_


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    categories = Category.query.order_by(Category.id).all()
    recommend_products = Product.query.filter(or_(Product.id == 1, Product.id == 5, Product.id == 9))
    return render_template('index.html', categories = categories, recommend_products=recommend_products)

@bp.route('/products/<int:categoryid>/')
def snowproducts(categoryid):
    products = Product.query.filter(Product.category_id == categoryid)
    return render_template('snowproduct.html', products = products)

#detailsのルート
@bp.route('/details/<int:productid>/')
def details(productid):
    product = Product.query.get(productid)
    return render_template('details.html', product = product)


@bp.route('/foundout/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    products = Product.query.filter(Product.name.like(search)).all()
    return render_template('snowproduct.html', products = products)




# Referred to as "Cart" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='',address='', totalcost=0,)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for product in order.products:
            totalprice = totalprice + product.price
    
    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your cart'
            return redirect(url_for('main.order'))
        else:
            flash('item already in cart')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)




# Delete specific cart items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap cart
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address = form.address.data
            totalcost = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your purchase! Your order has been completed!')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)


