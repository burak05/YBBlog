from distutils.log import debug
from flask import Flask,render_template, flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form, StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

# Register form
class RegisterForm(Form):
    name = StringField("Name Surname",validators=[validators.Length(min=4,max=25)])
    username = StringField("Username",validators=[validators.Length(min=5,max=35)])
    email = StringField("Email",validators=[validators.Email(message="Please enter a valid email address!")])
    password = PasswordField("Password: ",validators=[validators.DataRequired(message="Please enter a password!"),validators.EqualTo(fieldname="confirm",message="Passwords do not match!")])
    confirm = PasswordField("Confirm Password: ")



app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="ybblog"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__" :
    app.run(debug=True)