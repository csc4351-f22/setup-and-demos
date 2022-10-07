import flask
from nyt import get_headlines

app = flask.Flask(__name__)

@app.route("/")
def index():
    form_data = flask.request.args
    query = form_data.get("term", "Try Guys")
    headlines = get_headlines(query)
    return flask.render_template(
        "index.html",
        headlines=headlines
    )

app.run()