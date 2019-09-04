from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def greet_world():
    return render_template("index.html", goal="greet", name="World")

@app.route("/greet/<name>")
def greet_other(name):
    return render_template("index.html", goal="greet", name=name)

@app.route("/repeat/<num>/<name>")
def repeat_name(num, name):
    try:
        num = int(num)
    except ValueError:
        return "please follow the format '.../int/str"
    return render_template("index.html", goal="repeat", name=name, num=num)


if __name__=="__main__":
    app.run(debug=True)
