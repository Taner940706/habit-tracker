from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Habit tracker - Home")


@app.route('/add-habit', method=["GET", "Post"])
def add_habit():
    return render_template("add_habit", title="Habit tracker - Add habit")
