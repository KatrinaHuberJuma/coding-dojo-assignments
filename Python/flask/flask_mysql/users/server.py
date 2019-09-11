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
    
    return render_template("one_user.html", users=user)


@app.route("/users/create", methods=["POST"])
def add_user():
    mysql = connectToMySQL('users')
    query = """INSERT INTO users.users 
                (first_name, last_name, email, created_at, updated_at) 
                VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"""
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email']
    }
    user_id = mysql.query_db(query, data)
    route_str = "/users/" + str(user_id)

    return redirect(route_str)

@app.route("/users/<user_id>/edit")
def desplay_edit_page(user_id):
    mysql = connectToMySQL('users')
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': user_id
    }
    users = mysql.query_db(query, data)
    user = users[0]
    
    return render_template("edit_user.html", user=user)

@app.route("/users/<user_id>/update", methods=["POST"] )
def edit_user(user_id):
    print("line 27______", user_id)
    mysql = connectToMySQL('users')
    query = """UPDATE users.users
            SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, updated_at = NOW() 
            WHERE (id = %(id)s);"""
# UPDATE `users`.`users` SET `first_name` = 'Katrinahfvkjasfdh' WHERE (`id` = '4');

    data = {
        'id': user_id,
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email']
    }
    mysql.query_db(query, data)
    print(user_id)
    route_str = "/users/" + str(user_id)

    return redirect(route_str)


@app.route("/users/<user_id>/destroy")
def destroy_user(user_id):
    print("line 27______", user_id)
    mysql = connectToMySQL('users')
    query = """DELETE FROM users.users WHERE
            (id = %(id)s);"""
# UPDATE `users`.`users` SET `first_name` = 'Katrinahfvkjasfdh' WHERE (`id` = '4');

    data = {
        'id': user_id
    }
    mysql.query_db(query, data)

    return redirect("/users")



if __name__=="__main__":
    app.run(debug=True)
