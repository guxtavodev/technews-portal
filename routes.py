from flask import render_template, jsonify, redirect
from app import app 

@app.route("/")
def homepage():
  return render_template("index.html")
