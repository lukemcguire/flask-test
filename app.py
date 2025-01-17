from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci/<int:n>')
def get_fibonacci(n):
    return str(fibonacci(n))
