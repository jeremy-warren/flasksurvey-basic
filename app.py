from flask import Flask, render_template
from surveys import Question, Survey

app = Flask(__name__)

reponses = []


@app('/')
def rootpage()


render_template("base.html")
