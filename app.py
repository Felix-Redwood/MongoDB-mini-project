import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:MongoMongo1990@myfirstcluster-sdcsf.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    # Renders the tasks.html file and uses .find() to return everything in the tasks collection
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)