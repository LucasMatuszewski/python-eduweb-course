from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World !!! :)'


@app.route('/error')
def page_with_error():
    # We cen throw an error if we want with:
    raise ValueError  # In debug mode we will see nice Error description
    return 'This text won\'t be showed'


@app.route('/json-api')
def return_json():
    # To return anything as a json we just need jsonify from Flask
    return jsonify([{"name": "our json data"}])


# We can use two decorators with routes for one function:
@app.route('/greetings/')  # flask redirects to urls with slash on the end
# We can use variables from URL with <variable_name>
@app.route('/greetings/<name>')
def greetings(name="default user ;)"):
    return "Hi " + name


@app.route('/greetings/<name>/<surname>')
def full_greetings(name, surname):
    # from Python 3.6 we have something similar to template string in JS:
    return f"Hello {name.capitalize()} {surname.capitalize()}"


if __name__ == '__main__':
    app.run(debug=True)  # Debug mode adds Live-Restarting
