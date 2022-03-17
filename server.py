from flask import Flask, render_template, request, redirect, session
from user import User 
app = Flask(__name__) 


@app.route('/')                           
def index():
    return redirect('/users')  

@app.route("/users")
def users():
    return render_template("read.html", users = User.get_all())

@app.route('/create_user')
def new():
    return render_template("create.html")

@app.route('/create_user', methods = ["POST"])
def create_user(): # First we make a data dictionary from our request.form coming from our template.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "mail" : request.form["mail"],
    } 
    print(data)# First we make a data dictionary from our request.form coming from our template.
    User.save(data) # We pass the data dictionary into the save method from the Friend class.
    return redirect('/users') # Don't forget to redirect after saving to the database.


if __name__=="__main__":
    app.run(debug=True)                  




# @app.route('/read')                           
# def read():
#     return render_template('read.html')  

    








