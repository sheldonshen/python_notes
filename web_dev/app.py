'''
Created on Sep 20, 2016

@author: sheldonshen
'''
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)
#refactor code with MVC(jinja2)
@app.route("/",methods=['GET','POST'])
def home():
    #return "<h1>Home</h1>"
    return render_template("home.html")


@app.route("/signin",methods=["GET"])
def signin_form():
#     return '''<form action="/signin" method="post">
#                 <p><input name="username"></p>
#                 <p><input name="password" type="password"></p>
#                 <p><button type="submit">Sign in</button></p>
#              </form>'''
    return render_template("form.html")

@app.route("/signin",methods=['POST'])
def signin():
    #需要从request对象读取表单内容
    username=request.form['username']
    password=request.form['password']
    if  username== 'admin' and password=='password':
        #return "<h3>Hello,admin!</h3>"
        return render_template('signin-ok.html',username=username)
    #return '<h3>Bad username or password</h3>'
    return render_template("form.html",message="Bad username or password",username=username)

if __name__=='__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run()
