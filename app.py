from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey as survey
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = ['dogs']

# debug = DebugToolbarExtension(app)


responses = []

# the base page shows the survey and a start button


@app.route('/')
def start_survey():
    return render_template("/instructions.html")


@app.route('/questions/<int:qid>')
def show_question():
    return render_template("/question.html")


@app.route('/answer', methods="POST")
def next_question():
    choice = request.form['answer']
    responses.append(choice)
