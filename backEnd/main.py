from flask import Flask, jsonify, request
import json
import multiprocessing

class BackendGUI():
    def __init__(self,app):
        self.app = app

app = Flask(__name__) # create the flask app
backend = BackendGUI(app) # create the backend class object


'''
starts the water system with the given parameters
'''
@backend.app.route("/startSystem", methods=["POST"])
def startSystem():
    data = request.get_json() # get the data from the request
    with open("./backEnd/system.json", "w") as f:
        json.dump(data, f) # write the data to the system.json file

    return jsonify({"success": True}) # return success for frontend validation

@backend.app.route("/stopSystem", methods=["POST"])
def stopSystem():

    return jsonify({"success": True}) # return success for frontend validation

