from flask import Flask, render_template, request, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User
# ------------------------DISPLAY ROUTES-------------------------
@app.route("/")
def all_users():
    users = User.get_all()
    return render_template("all_users.html", users = users)

    # create user page ------------------------------------
@app.route("/create_user")
def new():
    return render_template("create_user.html")

    #show unique user page --------------------------------
@app.route("/show_user/<int:id>")
def show_user(id):
    data = {"id":id} 
    user = User.get_user(data)
    return render_template("show_user.html", user = user)

    #edit unique user page ---------------------------------
@app.route("/edit_user/<int:id>")
def edit_user(id):
    data = {"id":id}
    user = User.get_user(data)
    return render_template("edit_user.html", user = user)


# ------------------------ACTION ROUTES-------------------------

    #create a user
@app.route("/create_user", methods = ["POST"])
def create_user(): 
    print(request.form)
    User.save(request.form)
    return redirect('/') 

    #update a user
@app.route("/update_user", methods = ["POST"])
def update_user(): 
    print(request.form)
    User.update_user(request.form)
    return redirect('/') 

    #delete a user
@app.route('/delete_user/<int:id>/delete')
def delete_user(id):
    print(request.form)
    User.delete_user({"id":id})
    return redirect('/')
