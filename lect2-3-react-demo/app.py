import flask

app = flask.Flask(__name__)
app.secret_key = "blahbbb"

@app.route("/")
def main():
    return flask.render_template("index.html")


app.run(debug=True)