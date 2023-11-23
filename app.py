from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="web-app/front-end")


@app.route("/")
def index():
    return render_template("index.html")
