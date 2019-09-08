from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

@app.route("/")
def display_form():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def get_user_input():
    session['name'] = request.form['name']

@app.route("/")
def display_result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)