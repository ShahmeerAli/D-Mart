from flask import Flask, render_template
from data import Products

app = Flask(__name__)

Products = Products()

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/rice')
def products():
    return render_template("products.html", products = Products)


if __name__ == "__main__":
    app.run(debug=True)