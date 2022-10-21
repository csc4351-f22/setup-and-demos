import flask
from nyt import get_headlines

app = flask.Flask(__name__)

@app.route("/")
def index():
    # get all the query params from the request. This only works because the form in
    # index.html uses a GET and not a POST. If we used a POST, we would want to use
    # flask.request.form
    form_data = flask.request.args  
    # .get() is a method you can call with dictionaries that looks for a key and returns
    # a default if it's missing. So our query will be "Try Guys"" if there's no "term" in form_data
    query = form_data.get("term", "Try Guys")  
    headlines = get_headlines(query)
    return flask.render_template(
        "index.html",
        headlines=headlines
    )

app.run()