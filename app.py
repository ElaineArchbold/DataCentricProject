import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'HinchingJournal'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/todo')
def todo():
    return render_template('todo.html',
                           tasks=mongo.db.tasks.find(), categories=mongo.db.categories.find(), days=mongo.db.days.find())


@app.route('/addtodo')
def addtodo():
    return render_template('addtodo.html',
                           tasks=mongo.db.tasks.find(), categories=mongo.db.categories.find(), days=mongo.db.days.find())


@app.route('/updatetodo', methods=['POST'])
def updatetodo():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('todo'))


@app.route('/edittodo/<task_id>')
def edittodo(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    all_days = mongo.db.days.find()
    return render_template('edittodo.html',
                           task=the_task, categories=all_categories, days=all_days)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    task = mongo.db.tasks
    task.update({'_id': ObjectId(task_id)},
                {
        'day_id': request.form.get('day_id'),
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'products': request.form.get('products'),
        'how_to': request.form.get('how_to'),
        'is_complete': request.form.get('is_complete'),
    })
    return redirect(url_for('todo'))


@app.route('/completed/<task_id>')
def completed(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('todo'))


@app.route('/tips')
def tips():
    return render_template('tips.html')


@app.route('/shopping')
def shopping():
    return render_template('shopping.html')


@app.route('/products')
def products():
    return render_template('products.html',
                           products=mongo.db.products.find())


@app.route('/addproduct')
def addproduct():
    return render_template('addproduct.html',
                           products=mongo.db.products.find())


@app.route('/updateproduct', methods=['POST'])
def updateproduct():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for('products'))


@app.route('/editproduct/<product_id>')
def editproduct(product_id):
    the_product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template('editproduct.html',
                           product=the_product)


@app.route('/update_product/<product_id>', methods=["POST"])
def update_product(product_id):
    product = mongo.db.products
    product.update({'_id': ObjectId(product_id)},
                   {
        'product_name': request.form.getlist('product_name'),
    })
    return redirect(url_for('shopping'))


@app.route('/removeproduct/<product_id>')
def removeproduct(product_id):
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('shopping'))


@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
