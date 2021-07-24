from flask import Flask
app = Flask(__name__)

def makeBold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def makeEmphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def makeUnderline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


def makeH1(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p> This is a paragraph </p>' \
           '<img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width=200>'


@app.route("/bye")
@makeBold
@makeEmphasis
@makeUnderline
@makeH1
def bye():
    return "<p>Goodbye!</p>"


@app.route("/<name>")
def greet(name):
    return f"<p>Hello, {name} </p>"


#Create variable paths and convert the path to a data type
@app.route('/username/<name>/<int:number>')
def greetUser(name, number):
    return f'<h1 style="text-align:center">Hi {name}, you are {number} years old</h1>'


if __name__ == "__main__":
    app.run(debug=True)