from flask import Flask, flash, render_template, redirect, url_for, jsonify, request, session
import math

class BackendGUI():
    def __init__(self,app):
        self.app = app
        self.app.secret_key = open("./backEnd/supersecret.key").read()

app = Flask(__name__)
backend = BackendGUI(app)

@backend.app.route("/", methods=["GET"])
def index():
    return jsonify([{"Title":"World", "body": "the"}])

