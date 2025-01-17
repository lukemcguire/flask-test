from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1: int, num2: int) -> str:
    """Adds two numbers together.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The sum of the two numbers as a string.
    """
    return str(num1 + num2)

def fibonacci(n: int) -> int | str:
    """Calculates the nth Fibonacci number.

    Args:
        n: The index of the desired Fibonacci number.

    Returns:
        The nth Fibonacci number, or an error message if the input is invalid.
    """
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
def get_fibonacci(n: int) -> str:
    """Gets the nth Fibonacci number via the fibonacci function.

    Args:
        n: The index of the desired Fibonacci number.

    Returns:
        The nth Fibonacci number as a string.
    """
    return str(fibonacci(n))

if __name__ == '__main__':
    app.run(debug=True)
