from flask import Flask, render_template, url_for, request, session, redirect,flash
import pickle
import pyttsx3 
import threading 
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if  request.method == 'POST':
        a={'fontSize':request.form['fontSize'] , 'fontColor':request.form['fontColor'] , 'fontbgcolor':request.form['fontbgcolor'] , 'rpm':request.form['rpm']}
        with open('data.sm', 'wb') as handle:
            pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return redirect("/speech")
    with open('data.sm', 'rb') as handle:
        b = pickle.load(handle)
    return render_template('inputs.html',data=b)


@app.route('/speech', methods=['POST','GET'])
def speech():
    with open('data.sm', 'rb') as handle:
        b = pickle.load(handle)
    text="This is so cool!"
    return render_template('render.html',data=b,text=text)

if __name__ == '__main__':
    app.secret_key = 'my'
    app.run(debug=True)