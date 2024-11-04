from flask import Flask, request
import html
import os

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
    message = html.escape(request.args.get('q', ''))
    return {'message': message}


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
