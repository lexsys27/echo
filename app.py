import os
from flask import Flask, request


app = Flask(__name__)


@app.route('/echo')
def echo():
    """
    Retrieves a query parameter 'q' from the request arguments and returns it 
    in a dictionary.

    Returns:
        dict: A dictionary containing the 'message' key with the value of the
        'q' query parameter.
    """
    message = request.args.get('q', '')
    return {'message': message}


@app.route('/greet')
def greet():
    """
    Greets a user by name from the query parameter. Uses 'human' if no name 
    provided.

    Returns:
        dict: A dictionary containing the 'greeting' with personalized message.
    """
    name = request.args.get('name', 'human')
    return {'greeting': f'Hello, {name}!'}


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
