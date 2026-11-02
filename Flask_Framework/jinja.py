#building URL dynamically
#variable rule
#jinja 2  template engine

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#dynamic url
@app.route("/submit/<score>")
def score_display(score):
    return f"You have got {score} marks in maths"

#variable rule
@app.route("/pass/<int:score>")
def pass_score(score):
    return f"your passing score is {str(score)}"

#use of jinja template
@app.route("/result/<int:marks>")
def result_display(marks):
    if marks >= 50:
        res="passed"
    else:
        res="failed"
    return render_template("result_page.html", res=res) 

#example:2
@app.route("/display_result/<int:marks>") 
def display_result(marks):
    return render_template("result.html", marks=marks) 

#example:3
@app.route("/getresult", methods=['GET', 'POST'])
def get_result():
    avg_marks=0
    if request.method=="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])

        avg_marks = (science+maths+c)/3
    return redirect(url_for("display_result", marks=int(avg_marks)))

if __name__=="__main__":
    app.run(port=8000, debug=True)

