import os
import flask
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120))
    priority = db.Column(db.String(80))
    due_date = db.Column(db.String(80))

with app.app_context():
    db.create_all()


@app.route("/delete", methods=["POST"])
def delete():
    # Gross! The request data (which comes from the "body" arg we gave to fetch())
    # comes to us as bytes instead of a string, so we have to call decode()
    # Even then, it's JSON data (which means it has quotes around it, but in more
    # complex examples, it would mean we'd get a string representation of a JSON object
    # instead of a JSON object), so we also have to call json.loads().

    # This isn't exactly "hacky" (it makes sense when you think through it),
    # but I think this was more content than I could realistically ask you 
    # all to pick up from one lecture.
    description_to_delete = json.loads(flask.request.data.decode())
    to_delete = Todo.query.filter_by(task=description_to_delete).first()
    db.session.delete(to_delete)
    db.session.commit()
    return flask.redirect("/")

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        data = flask.request.form
        new_todo = Todo(
            task=data["task"], priority=data["priority"], due_date=data["due_date"]
        )
        db.session.add(new_todo)
        db.session.commit()

    todos = Todo.query.all()
    num_todos = len(todos)
    return flask.render_template(
        "index.html",
        num_todos=num_todos,
        todos=todos,
    )


app.run(debug=True)