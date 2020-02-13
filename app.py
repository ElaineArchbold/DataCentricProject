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
@app.route('/todo')
def todo():
    return render_template('todo.html',
                           tasks=mongo.db.tasks.find())


@app.route('/addtodo')
def addtodo():
    return render_template('addtodo.html',
                           categories=mongo.db.categories.find())


@app.route('/updatetodo', methods=['POST'])
def updatetodo():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('todo'))


@app.route('/home')
def home():
    return render_template('home.html')


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
