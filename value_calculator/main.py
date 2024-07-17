import html
from flask import Flask, render_template
import PVcal

app = Flask(__name__)

@app.route("/")
def pv(FV, Y, I, k):
    return

if __name__ == "__main__":
    app.run(debug=True)