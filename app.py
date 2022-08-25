from flask import Flask, render_template, request, session, redirect, flash
from surveys import satisfaction_survey as survey
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = ['dogs']

# debug = DebugToolbarExtension(app)


responses = []

# the base page shows the survey and a start button


@app.route('/')
def load_base():
    return render_template("/instructions.html", survey=survey)


@app.route('/start', methods=['POST', 'GET'])
def load_first_question():

    return redirect('question/0.html')


@app.route('/question/<int:qid>')
def show_question(qid):
    if qid == len(responses):
        question = survey.questions[qid]
        return render_template("/question.html/", question_num=qid, question=question)
    else:
        flash(f"No skipping around, please!")
        return redirect(f"/question/{len(responses)}")


@app.route('/answer', methods=["POST", "GET"])
def next_question():
    choice = request.form['answer']
    responses.append(choice)
    if len(responses) == len(survey.questions):
        return render_template("thank_you.html")
    elif len(responses) < len(survey.questions):
        return redirect(f"question/{len(responses)}")
