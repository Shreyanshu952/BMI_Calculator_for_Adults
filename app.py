#BMI Calculator for Adults

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/calculate.bmi", methods = ["POST", "GET"])
def calculate_bmi():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        weight = float(request.form["Weight"])
        height = float(request.form["Height"])

        BMI = weight / (height ** 2)

        BMI_adults = round(BMI, 1)

        age = float(request.form["Age"])

        return render_template("result.html", Age = age, results = BMI_adults)

if __name__=="__main__":
    app.run(debug=True)