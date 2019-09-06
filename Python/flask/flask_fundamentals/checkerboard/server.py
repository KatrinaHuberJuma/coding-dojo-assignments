from flask import Flask, render_template
from color_v_num import what_is_this
app = Flask(__name__)


@app.route("/")
@app.route("/<w>/<x>/<y>/<z>/")
def make_board(w=8, x=8, y='green', z='black' ):
    color1 = y
    color2 = z
    num1 = 8
    num2 = 8
    

    return render_template("index.html", color1=color1, color2=color2, num1=num1, num2=num2)




if __name__=="__main__":
    app.run(debug=True)
