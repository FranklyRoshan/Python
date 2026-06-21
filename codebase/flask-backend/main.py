import os
from flask import Flask

# Initialize the Flask application
# __name__ helps Flask locate resources like templates and static files
app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Root route that returns a simple HTML welcome message.
    """
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

if __name__ == "__main__":
    # Retrieve the port from environment variables, defaulting to 5000
    port = int(os.environ.get("MINIKUBE_PORT", 5000))

    # Run the application locally
    # Setting debug=True enables automatic code reloading and a browser debugger
    app.run(host="127.0.0.1", port=port, debug=True)
