from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)


def get_random_phrase(filename):
    with open(filename, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        return random.choice(lines) if lines else "Talia says hi!"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answer = request.form.get('car_question', '').strip().lower()
        if answer == 'sparkles':
            return redirect(url_for('talia'))
    phrase = get_random_phrase('data/talisms.txt')
    return render_template('index.html', phrase=phrase)


@app.route('/talia')
def talia():
    quote = get_random_phrase('data/love_sab.txt')
    birthday_message = ""
    if os.path.exists('data/birthday.txt'):
        with open('data/birthday.txt', encoding='utf-8') as f:
            birthday_message = f.read()
    return render_template('talia.html', quote=quote, birthday=birthday_message.replace('\n', '<br>'))


if __name__ == '__main__':
    app.run(debug=True)
