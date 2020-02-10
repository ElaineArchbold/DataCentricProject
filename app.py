import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'HinchingJournal'

mongo = PyMongo(app)


@app.route('/')
def hello():
    return "hello there you beaut"


@app.route('/todo')
def todo():
    return render_template("todo.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
