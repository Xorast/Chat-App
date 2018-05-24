import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def get_index():
    return "Welcome to our chat !"
    
@app.route("/<username>")
def get_userpage(username):
    return "Hello " + username

@app.route("/<username>/<message>")
def add_message(username, message):
    # return "<strong>" + username +"</strong>" + " : " + message
    return "<strong>{0}: </strong>{1}".format(username, message)
    


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)

