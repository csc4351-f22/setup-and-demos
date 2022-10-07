import flask
import random

app = flask.Flask(__name__)

@app.route("/")
def index():
    num = random.randint(1, 10)
    return flask.render_template(
        "index.html",
        number=num
    )

app.run(debug=True)