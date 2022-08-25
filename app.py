from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = ['dogs']


responses = []

# the base page shows the survey and a start button


@app.route('/')
def start_survey():

    return redirect("/instructions.html")


@app.route('/instructions', methods='POST')
def instructions():
    return render_template("instructions.html")
    responses = []


@app.route('/questions/<int:qid>', methods='POST')
def questions():
    return render_template('questions/qid.html')
    if not responses[0]:
        print('lakdslalsjd')
