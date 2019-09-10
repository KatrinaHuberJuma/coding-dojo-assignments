from flask import Flask, redirect, render_template
from connection import connectToMySQL

app = Flask(__name__)


@app.route("/")
def display_index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db("SELECT * FROM pets;")
    return render_template("index.html", pets=pets)


@app.route("/add_pet", methods=["POST"])
def add_pet():
    query = "INSERT INTO `pets`.`pets` (`name`, `type`) VALUES (%(name)s, %(type)s);"

if __name__=="__main__":
    app.run(debug=True)
