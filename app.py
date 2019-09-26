from flask import Flask
from flask import render_template,request,url_for,redirect
import smtplib as smtp


appl = Flask(__name__)
@appl.route("/")
def first():
    return render_template("first.html")

if __name__=='__main__':
    appl.run(debug=True,port=80)