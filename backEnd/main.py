from flask import Flask, jsonify, request
import json
import multiprocessing
import driver


class BackendGUI():
    def __init__(self, app):
        self.app = app
        self.multithread = None


app = Flask(__name__)  # create the flask app
backend = BackendGUI(app)  # create the backend class object

'''
starts the water system with the given parameters
'''


@backend.app.route("/startSystem", methods=["POST"])
def startSystem():
    data = request.get_json()  # get the data from the request
    with open("./backEnd/system.json", "w") as f:
        json.dump(data, f)  # write the data to the system.json file

    backend.multithread = multiprocessing.Process(target=driver.main, args=(data,))  # create a new process
    backend.multithread.start()  # start the system

    return jsonify({"success": True})  # return success for frontend validation


@backend.app.route("/stopSystem", methods=["POST"])
def stopSystem():
    backend.multithread.terminate()  # terminate the process
    backend.multithread.join()  # wait for the process to finish
    backend.multithread = None  # reset the process
    return jsonify({"success": True})  # return success for frontend validation
