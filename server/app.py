from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string passed as a parameter in the console and display it in the browser
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print the string to the console
    return text  # Display the string in the web browser

# Route to display numbers from 0 to the passed parameter on separate lines
@app.route('/count/<int:number>')
def count(number):
    # Return numbers separated by newlines, as required for the tests
    return '\n'.join(str(i) for i in range(number)) + '\n'

# Route to perform mathematical operations on two numbers
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the correct mathematical operation based on the parameter passed
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Handle division by zero and return a meaningful result
        result = num1 / num2 if num2 != 0 else 'undefined (division by zero)'
    elif operation == '%':
        result = num1 % num2
    else:
        # Handle invalid operations
        result = 'Invalid operation'

    return str(result)  # Display the result in the web browser

# Run the app with custom port and debugging enabled
if __name__ == '__main__':
    app.run(port=5555, debug=True)
