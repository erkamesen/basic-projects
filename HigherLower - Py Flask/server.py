from flask import Flask
import random
app = Flask(__name__)



def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def make_emphasis(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def make_udnerline(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


num = random.randint(0,9)
@app.route("/<int:number>")
def guess(number):
    if number == num:
        return "<h1 style='color:green;'> You find me :)</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>" \

    if number > num:
        return "<h1 style='color:Tomato;'> Too high, try again !</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < num:
        return "<h1 style='color:purple;'> Too low, try again !</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"






















if __name__ == "__main__":
    app.run(debug=True)


