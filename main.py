from flask import Flask, request, jsonify, render_template
import os, requests, json
from api import api

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
