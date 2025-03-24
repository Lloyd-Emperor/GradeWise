from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_average_score(scores):
    return sum(scores) / len(scores)

def assign_grade(average_score):
    if average_score >= 80:
        return "A"
    elif average_score >= 70:
        return "B"
    elif average_score >= 60:
        return "C"
    elif average_score >= 50:
        return "D"
    else:
        return "F"

def provide_feedback(grade):
    feedback = {
        "A": "Excellent performance! Keep it up.",
        "B": "Good job! You can do even better.",
        "C": "Fair effort! Work harder next time.",
        "D": "Needs improvement. Keep practicing.",
        "F": "Poor performance. Seek help and try again."
    }
    return feedback[grade]

@app.route("/", methods=["GET", "POST"])
def index():
    current_year = datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        student_id = request.form.get("id")

        scores = []
        for i in range(1, 6):
            score = float(request.form.get(f"score{i}"))
            scores.append(score)

        average_score = calculate_average_score(scores)
        grade = assign_grade(average_score)
        feedback = provide_feedback(grade)

        return render_template(
            "results.html",
            name=name,
            age=age,
            student_id=student_id,
            scores=scores,
            average_score=average_score,
            grade=grade,
            feedback=feedback,
            year=current_year
        )
    return render_template("index.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
