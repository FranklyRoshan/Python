from flask import Flask, render_template

apps = Flask(__name__)

@apps.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
   apps.run(debug=True)