from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()
