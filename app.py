from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        name = request.form["name"]

        marks = [
            float(request.form["sub1"]),
            float(request.form["sub2"]),
            float(request.form["sub3"]),
            float(request.form["sub4"]),
            float(request.form["sub5"])
        ]

        total = sum(marks)
        average = total / 5

        if average >= 90:
            grade = "A"
            message = "Excellent Performance!"
        elif average >= 75:
            grade = "B"
            message = "Great Performance! "
        elif average >= 60:
            grade = "C"
            message = "Good Performance! "
        elif average >= 50:
            grade = "D"
            message = "Keep Improving! "
        else:
            grade = "F"
            message = "More Practice Needed ."

        result = {
            "name": name,
            "total": total,
            "average": round(average, 2),
            "grade": grade,
            "message": message
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)