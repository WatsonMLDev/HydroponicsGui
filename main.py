from flask import Flask, flash, render_template, redirect, url_for, jsonify, request, session

class BackendGUI():
    def __init__(self,app):
        self.app = app
        self.app.secret_key = open("supersecret.key").read()

app = Flask(__name__)
backend = BackendGUI(app)

@backend.app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
