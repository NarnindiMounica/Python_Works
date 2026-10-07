# import sys
# print("Running with interpreter:", sys.executable)

from flask import Flask

'''
It creates an instance of flask class,
which will be your WSGI (Web Server Gateway Interface) application'''

#WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return 'Welcome Here !!!'

if __name__=="__main__":
    app.run(port=8000, debug=True)
