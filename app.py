from flask import Flask, render_template, request, redirect, url_for
from parse_question import parsed_questions
import model
from mbti import mbti_types

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html", questions=parsed_questions)

@app.route("/result", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        answers = []
        for i in range(50):
            answers.append(
                request.form.get("answer[" + str(i) + "]")
            )
        
        type = model.predict(answers)
        desc = mbti_types[type]
        
        return render_template("result.html", type=type, desc=desc)
    else:
        return render_template("result.html")
        # redirect(url_for("index"))