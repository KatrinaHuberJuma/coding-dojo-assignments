from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)


app.secret_key = "akjsdhfadhsfkjashdfkjashfjkashfajklsfhakjsdhf"

@app.route("/")
def display_form():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def get_user_input():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")


@app.route("/result")
def display_result():
    return render_template("result.html", name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])


if __name__ == "__main__":
    app.run(debug=True)