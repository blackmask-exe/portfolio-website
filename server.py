"""Server side for the template of the portfolio website"""
from flask import Flask, abort, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "hururururuurur"

@app.route("/", methods=["POST", "GET"])
def homepage():
    """Homepage for the portfolio website"""
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
