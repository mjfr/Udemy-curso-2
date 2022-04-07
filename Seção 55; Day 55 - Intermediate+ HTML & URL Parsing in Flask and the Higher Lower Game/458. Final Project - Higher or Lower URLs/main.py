from flask import Flask, request
from random import randint

app = Flask(__name__)


def generate_random():
    return randint(0, 9)


random_number = generate_random()


@app.route("/")
def initial_page():
    return "<h1>Guess a number between 0 and 9</h1><br>" \
           "<img src=\"https://media.giphy.com/media/65S6VhtQucbE8tBZEV/giphy.gif\">" \
           "<br><br>" \
           "<form action=\"/verify_number\" method=\"post\" enctype=\"multipart/form-data\">" \
           "<label for=\"guess\">Your guess: </label>" \
           "<input type=\"text\" id=\"guess\" name=\"guess\" placeholder=\"Your answer\" autofocus>" \
           "<input type=\"submit\" value=\"Submit\">" \
           "</form>"


@app.route(f"/verify_number", methods=["GET", "POST"])
def verify_number():
    number = int(request.form.get("guess"))
    global random_number
    if random_number == int(number):
        random_number = generate_random()
        print(random_number)
        return "<img src=\"https://media.giphy.com/media/etKSrsbbKbqwW6vzOg/giphy.gif\">" \
               "<h3>Want to play again?</h3>" \
               "<a href=\"/\">Yes</a>"
    if random_number > int(number):
        return "<img src=\"https://media.giphy.com/media/3oFzmko6SiknmpR2NO/giphy.gif\">" \
               "<p>Your guess is <strong>lower</strong> than the number. More luck on the next time.</p>" \
               "<h3>Want to play again?</h3>" \
               "<a href=\"/\">Yes</a>"
    if random_number < int(number):
        return "<img src=\"https://media.giphy.com/media/3oFzmko6SiknmpR2NO/giphy.gif\">" \
               "<p>Your guess is <strong>higher</strong> than the number. More luck on the next time.</p>" \
               "<h3>Want to play again?</h3>" \
               "<a href=\"/\">Yes</a>"


if __name__ == '__main__':
    app.run(debug=True)
