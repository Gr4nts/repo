from flask import Flask, Blueprint, jsonify, render_template, request
import os, requests, json

api = Blueprint("api", __name__)

# This endpoint takes in 'POST' data and assigns it to 'patients'
@api.route("/", methods = ["GET", "POST"])
def showPatient():
    patients = request.json['patient']
    return jsonify(patients)

# This endpoint statically assigns newPatient to the values provided, then prints them to a new file called patients.json
@api.route("/add",  methods = ["GET", "POST"])
def addPatient():
    newPatient = [
        "Johnathon",
        "52 Smith Street",
        "3849038493849",
        "Dead"
]
    with open('patients.json', 'w') as f:
        json.dump(newPatient, f,indent=2)

    return render_template('index.html')
    
