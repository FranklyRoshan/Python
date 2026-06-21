from flask import Flask, session
import random

app = Flask(__name__)
# A secret key is required to use Flask sessions for data security
app.secret_key = "super_secret_flash_game_key"


@app.route('/')
def home():
    # Generate and store the random number in the user's session cookie
    # so it stays the same until they win or refresh the home page.
    session['random_number'] = random.randint(0, 9)
    print(f"Target Number for this session: {session['random_number']}")  # For debugging

    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    # Retrieve the stored number, default to 0 if they skipped the homepage
    target = session.get('random_number', 0)

    if guess > target:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < target:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
                
    else:
        return "<h1>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>" \
               "<p><a href='/'>Play Again?</a></p>"


if __name__ == "__main__":
    app.run(debug=True)