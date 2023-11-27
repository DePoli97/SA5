from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="front-end/scrappy")


@app.route("/")
def index():
    return render_template("/public/index.html")
