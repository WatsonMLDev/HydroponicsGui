from flask import Flask, flash, render_template, redirect, url_for, jsonify, request, session

class BackendGUI():
    def __init__(self, *args, **kwargs):
        self.app = Flask(__name__)
        self.app.secret_key = open("supersecret.key").read()


    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("view/index.html")
