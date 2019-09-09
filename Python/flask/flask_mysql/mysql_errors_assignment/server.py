from flask import Flask, render_template
from mysqlconn import connectToMySQL

app = Flask(__name__)

@app.route("/")
def display_index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)