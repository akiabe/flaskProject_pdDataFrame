import flask
from flask import render_template
from flask import send_file
import pandas as pd

app = flask.Flask(__name__)

df = pd.read_csv("static/sample.csv")
header = df.columns
record = df.values.tolist()

@app.route('/')
def index():
    return render_template(
        "index.html",
        header=header,
        record=record
    )

@app.route('/download')
def download():
    path = "static/sample.csv"
    return send_file(
        path,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
