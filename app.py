from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)
