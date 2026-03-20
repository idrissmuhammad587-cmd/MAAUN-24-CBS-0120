from flask import Flask, render_template, request
from models import Question, Result

app = Flask(_name_)

# Question list (STACK example)
questions = [
    Question("Capital of Nigeria?", ["Lagos", "Abuja", "Kano"], "Abuja"),
    Question("2 + 2 =", ["3", "4", "5"], "4"),
    Question("Color of the sky?", ["Blue", "Green", "Red"], "Blue")
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, q in enumerate(questions):
        answer = request.form.get(f"q{i}")
        if q.check_answer(answer):
            score += 1

    result = Result(score)

    return render_template("result.html", score=score, time=result.time)


if _name_ == "_main_":
    app.run(debug=True)