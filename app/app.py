from flask import Flask, request, render_template
import joblib
import numpy as np

model = joblib.load('models/dumped_models/best_model.joblib')
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trtbps = int(request.form["trtbps"])
        chol = int(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalachh = int(request.form["thalachh"])
        exng = int(request.form["exng"])
        oldpeak = float(request.form["oldpeak"])
        slp = int(request.form["slp"])
        caa = int(request.form["caa"])
        thall = int(request.form["thall"])

        input_data = np.array([[
            age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall
        ]])
        
        result = int(model.predict_proba(input_data)[0][1] * 100)
        if result % 10 == 0:
            result = f'<{result + 5}' if result + 5 < 100 else 'практически 100%. Обратитесь к врачу'
        else:
            result = f"{result - (result % 10)}-{result + (10 - (result % 10))}"
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)

if __name__ == '__main__':
    app.run(debug=True)
