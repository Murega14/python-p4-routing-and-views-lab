#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(f'{text}')
    return text

@app.route('/count/<int:number>')
def count(number):
    count = ""
    for i in range(number):
        count += f'{i}\n'
    return count

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid number format", 400

    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return "Division by Zero is NOT ALLOWED", 400
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return "Invalid operation", 400
        
        if operation == 'div':
            result = f"{result:.1f}"
        else:
            if result.is_integer():
                result = int(result)
            else:
                result = str(result)

        return str(result)
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(port=5555, debug=True)
