import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

all_the_messages = []

@app.route("/")                                                                 # when the client is at the location "/" ,
def show_landing_page():                                                        # do : 
    return render_template("index.html")                                        # render template that is in the templates folder, called "index.html"

@app.route("/login")                                                            # when the client is at the location "/login"
def get_username():                                                             # do :
    username = request.args.get('username')                                     # username = request.args['username'] // Get the value of the argument 'username'
                                                                                # the form send an URL/request with /login?username="..."&color="..." ==> flask got it. ? : request
    return redirect(username)                                                   # gonna redirect to "/" + username. the "/" is implicit. 
                                                                                # if we wanted to have the path username/color ==> redirect(username + "/" + color)
    
@app.route("/<username_II>")
def get_userpage(username_II):                                                  # here, the argument "username_II" is coming from the "<username_II>"
    return render_template("chat.html", logged_in_as=username_II, post = all_the_messages)               # enable to have a variable into the new page

# @app.route("/<username>/<message>")
# def add_message(username, message):
#     return "<strong>{0}: </strong>{1}".format(username, message)
    
@app.route("/<username_III>/new", methods=["POST"])
def post_message(username_III):
    text    = request.form["message"]
    # message = "<strong>{0}:</strong> {1}".format(username_III, text)          # changement du data structure
    
    message = {
        'sender': username_III,
        'body': text
    }
    
    all_the_messages.append(message)
    return redirect(username_III)
    




app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)