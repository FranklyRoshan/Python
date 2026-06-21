from flask import Flask

app = Flask(__name__)


def make_bold(original_func):
    def wrapper_func():
        return f'<b>{original_func()}</b>'

    return wrapper_func


def make_emphasis(original_func):
    def wrapper_func():
        return f'<em>{original_func()}</em>'

    return wrapper_func


def make_underlined(original_func):
    def wrapper_func():
        return f'<u>{original_func()}</u>'

    return wrapper_func


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: left">Hello, world!</h1>'
            '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDhqdmd2d3BhdGVtczN1NDhuaWxwdnlqNXY3bXR4aGs4ZWdocGt5eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3z3Jqt42yS104gRc5c/giphy.gif", width=200>')


# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


# Creating variable paths and converting the path to a specified date type
@app.route('/username/<name>/<int:number>')
def great(name, number):
    return f'Hello {name}!, you are {number} years old!'


# username/<name>
# username/<name>/1
# username/<path:name>
# username/<name>/<int:number>

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
