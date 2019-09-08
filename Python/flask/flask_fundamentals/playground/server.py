from flask import Flask, render_template
app = Flask(__name__)



@app.route("/play/")
@app.route("/<color>/<num>/")
def playground(num='3', color='blue'):   
    try:
        num = int(num)
    except ValueError:
        return "please follow the format '.../color/int"

    return render_template("index.html", color=color, num=num)


if __name__=="__main__":
    app.run(debug=True)
