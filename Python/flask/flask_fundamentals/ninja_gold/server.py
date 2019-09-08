from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)


app.secret_key = "akjsdhfadhsfkjashdfkjashfjkashfajklsfhakjsdhf"

@app.route("/")
def display_home():
    if "gold" not in session:
        session['gold'] = 0
    print(session['gold'])
    return render_template("index.html", gold=session['gold'])

@app.route("/process", methods=["POST"])
def process_form():
    if request.form['location'] == 'farm':
        session['gold'] += random.choice([10, 15, 20])
    elif request.form['location'] == 'cave':
        session['gold'] += random.choice([5, 10])
    elif request.form['location'] == 'house':
        session['gold'] += random.choice([2, 3, 4, 5])
    else:
        session['gold'] += random.choice([20, -20])
    
    return redirect("/")

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)