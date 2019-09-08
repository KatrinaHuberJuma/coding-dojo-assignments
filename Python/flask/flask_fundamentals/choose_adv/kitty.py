from flask import Flask,render_template, render_template, request
app = Flask(__name__)

@app.route('/')
def lost_kitty():
    return render_template('Start.html')

@app.route('/backtrack')
def backtrack():
    return render_template('backtrack.html')

@app.route('/follow_butterfly')
def follow_butterfly():
    return render_template('follow_butterfly.html')

@app.route('/follow_person')
def follow_person():
    return render_template('/follow_person.html')

@app.route('/home')
def home():
    return render_template('/home.html')

# @app.route('/be_adorable')
# def be_adorable():
#     return render_template('/be_adorable.html')

@app.route('/new_home')
def new_home():
    return render_template('/new_home.html')    

if __name__=="__main__":
    app.run(debug=True)
