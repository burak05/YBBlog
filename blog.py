from distutils.log import debug
from flask import Flask,render_template, flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form, StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route("/")
def index():
    article = dict()
    article["Title"] = "Title"
    article["Body"] = "Body"
    article["Author"] = "Author"
    return render_template("index.html",article = article)

if __name__ == "__main__" :
    app.run(debug=True)