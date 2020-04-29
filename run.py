from flask import Flask, render_template, redirect, url_for
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.fields import (StringField, SubmitField, FileField)
from flask_wtf import Form
import sqlite3
from data import Products

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


Products = Products()

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products', methods=["GET", "POST"])
def products():
    form = UploadForm()
    return render_template("products.html", form  = form )

class UploadForm(Form):
    file = FileField()
    submit = SubmitField("submit")


@app.route('/grocery')
def grocery():
    return render_template("grocery.html")


if __name__ == "__main__":
    app.run(debug=True)