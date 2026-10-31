#building URL dynamically
#variable rule
#jinja 2  template engine

from flask import Flask, render_template, request

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
        res="pass"
    else:
        res="fail"
    return render_template("result_page.html", res=res)      
        

if __name__=="__main__":
    app.run(port=8000, debug=True)

