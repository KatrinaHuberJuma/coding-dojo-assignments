from flask import Flask, render_template, flash, request, redirect, session
import secret
app = Flask(__name__)

app.secret_key = secret.key 


@app.route('/name_kitty', methods=['POST'])
def name_kitty():
    session['name'] = request.form['kittyname']
    print(session['name'])
    return redirect('/')


@app.route('/')
def lost_kitty():
    print("losing kitty")
    try:
        if not session['name']:
            session['name'] =False
    except:
        session['name'] =False
   
    try:
        session['num_starts'] +=1
        num = session['num_starts']
    except KeyError:
        print("in except case")
        session['num_starts'] = -1
        num = session['num_starts']
    return render_template('start.html', name=session['name'], num=session['num_starts'])

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

@app.route('/new_home')
def new_home():
    return render_template('/new_home.html')    

if __name__=="__main__":
    app.run(debug=True)
