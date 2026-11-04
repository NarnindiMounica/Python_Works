#Put and Delete - HTTP verbs
# Working with API's Json

from flask import Flask, jsonify, request

app = Flask(__name__)

#Initial data in my To-Do list
items = [{"id": 1, "name": "item 1", "description": "this is item 1"}, 
         {"id": 2, "name": "item 2", "description": "this is item 2"},
         {"id": 3, "name": "item 3", "description": "this is item 3"}]

@app.rooute("/")
def home():
    return "Welcome to the sample to-do list app"

#get: retrieve all items
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

#get: retrieve a specific item by id
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item == None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

#post: create a new task
@app.route("/items", methods=['POST'])
def 
