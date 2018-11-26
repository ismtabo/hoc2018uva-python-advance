from flask import Flask, render_template
app = Flask(__name__)

name = None # Replace with your name

@app.route('/')
def hello_world():
    return render_template('index.html', name=name)