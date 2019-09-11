from flask import Flask, redirect, render_template, request
from connection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def direct_root():
    return redirect("/users")


@app.route("/users")
def display_all():
    mysql = connectToMySQL('users')
    users = mysql.query_db("SELECT * FROM users;")
    return render_template("index.html", users=users)


@app.route("/users/new")
def display_new_user_form():
    mysql = connectToMySQL('users')
    users = mysql.query_db("SELECT * FROM users;")
    return render_template("new_user_form.html", users=users)


@app.route("/users/<user_id>")
def display_one_user(user_id):
    print("line 27______", user_id)
    mysql = connectToMySQL('users')
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': user_id
    }
    user = mysql.query_db(query, data)
    
    return render_template("one_user.html", user=user)


@app.route("/users/create", methods=["POST"])
def add_user():
    mysql = connectToMySQL('users')
    query = "INSERT INTO `users`.`users` (`first_name`, `last_name`, 'email') VALUES (%(fn)s, %(ln)s, %(em)s,);"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email']
    }
    user = mysql.query_db(query, data)
    print(user)
    return redirect("/users/<user_id>", user_id = user.id)

if __name__=="__main__":
    app.run(debug=True)
