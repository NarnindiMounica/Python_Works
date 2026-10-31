from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/index", methods=['GET'])
def index_func():
    return render_template('index.html')

@app.route("/form", methods=['GET', 'POST'])
def form_func():
    
    
if __name__=="__main__":
    app.run(port=8000, debug=True)