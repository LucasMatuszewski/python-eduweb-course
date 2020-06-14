# Very simple Hello World App with Flask framework:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    # We cen throw an error if we want with:
    # raise ValueError # In debug mode we will see nice Error description
    return 'Hello, World !!! :)'

# to run this app either call a file app.py and run 'flask run' in the same folder, or...
# add ENV on your system with a path to a file with app. On PowerShell (in eduweb-python folder):
#   $env:FLASK_APP = "flask_web\hello.py"

# Next start server with:
#   flask run

# But this is very simple development server, not recommended on production.
#
# Now we run server without live-refreshing and without auto-restarting on change.
# We have to stop a server and run it again to see any changes in our file...


# THE EASIEST WAY:
# Add "app.run()" to the file and run this file in your IDE by pressing Play icon:
if __name__ == '__main__':
    # app.run() # Normal run without Live-Restarting
    app.run(debug=True)  # Debug mode adds Live-Restarting
