#building URL dynamically
#variable rule
#jinja 2  template engine

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/submit/<score>")
def score_display(score):
    return f"You have got {score} marks in maths"

if __name__=="__main__":
    app.run(port=8000, debug=True)

