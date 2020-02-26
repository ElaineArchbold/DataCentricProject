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
                           tasks=mongo.db.tasks.find(), categories=mongo.db.categories.find(), days=mongo.db.days.find(), products=mongo.db.products.find())


@app.route('/addtodo')
def addtodo():
    return render_template('addtodo.html',
                           tasks=mongo.db.tasks.find(), categories=mongo.db.categories.find(), days=mongo.db.days.find(), products=mongo.db.products.find())


@app.route('/updatetodo', methods=['POST'])
def updatetodo():
    tasks = mongo.db.tasks
    tasks.insert(request.form.to_dict())
    return redirect(url_for('todo'))


@app.route('/edittodo/<task_id>')
def edittodo(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    all_days = mongo.db.days.find()
    all_products = mongo.db.products.find()
    return render_template('edittodo.html',
                           task=the_task, categories=all_categories, days=all_days, products=all_products)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    task = mongo.db.tasks
    task.update({'_id': ObjectId(task_id)},
                {
        'day_id': request.form.get('day_id'),
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'product_name': request.form.get('product_name'),
        'how_to': request.form.get('how_to'),
    })
    return redirect(url_for('todo'))


@app.route('/completed/<task_id>')
def completed(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('todo'))


@app.route('/tips')
def tips():
    return render_template('tips.html')


@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
