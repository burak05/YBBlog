from distutils.log import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    sayi = 10
    return render_template("index.html",number=sayi)

if __name__ == "__main__" :
    app.run(debug=True)