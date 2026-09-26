import sys
print("Running with interpreter:", sys.executable)

from flask import Flask

'''
It creates an instance of flask class,
which will be your WSGI (Web Server Gateway Interface) application'''

app = Flask()