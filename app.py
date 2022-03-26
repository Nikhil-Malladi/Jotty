from flask import Flask
from flask import render_template
from flask import request

from web_app_functions import Playground

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Home!</h1>'

@app.route('/register',methods=["GET","POST"])
def register():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        P = Playground(username,email,password)
        resp = P.createUser()
        msg=resp['message']
    return render_template('register.html',msg=msg)

@app.route('/login',methods=["GET","POST"])
def login():
    msg=''
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        P = Playground(email=email,password=password)
        resp = P.verifyUser()
        if resp['status_code']==1:
            return render_template('index.html',msg=msg)
        else:
            msg=resp['message']
    return render_template('login.html',msg=msg)

if __name__=='__main__':
    app.run()
