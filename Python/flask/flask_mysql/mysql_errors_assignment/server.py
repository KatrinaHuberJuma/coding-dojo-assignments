from flask import Flask, render_template, request, redirect
from mysqlconn import connectToMySQL

app = Flask(__name__)

@app.route("/")
def display_index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db("SELECT * FROM friends;")
    # print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'oc': request.form['occ']
    }
    query = "INSERT INTO friends (first_name, last_name, occupation, create_time, update_time) VALUES (%(fn)s, %(ln)s, %(oc)s, NOW(), NOW());"
    print(query)
    mysql = connectToMySQL('friends')
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)