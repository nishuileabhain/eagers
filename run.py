"""
this is main app to be run
"""

import os  #  module for modifying directories
import json
from flask import Flask, render_template, request, flash  # import Flask class from flask module
if os.path.exists("env.py"):
    import env

myApp = Flask(__name__)
myApp.secret_key = os.environ.get("SECRET_KEY")


@myApp.route("/")  # decorator which wraps functions
def index():
    """ the homepage """
    return render_template("index.html")


@myApp.route("/about")
def about():
    """ the about page """
    return render_template("about.html", page_title="About")


@myApp.route("/contact", methods=["GET", "POST"])
def contact():
    """ takes information from the contact form """
    if request.method == "POST":
        flash("Thanks {}. We have received your message!".format(
            request.form.get("name")))
        print(request.form.get("name"))
        print(request.form.get("email"))
        print(request.form.get("message"))
    return render_template("contact.html", page_title="contact")


#  can i say active is true for a given page? Do i want to?
@myApp.route("/tricks")
def tricks():
    """ refers to a main page holding all the tricks """
    data = []
    with open("data/tricks.json", "r") as my_json_data:
        data = json.load(my_json_data)
    return render_template("tricks.html", page_title="tricks", tricks=data)


@myApp.route("/tricks/<trick_name>")
def about_trick(trick_name):
    """ refers to each individual trick """
    trick_detail = {}
    with open("data/tricks.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == trick_name:
                mytrick = obj
    return render_template("trick_detail.html", trick_detail=mytrick)


if __name__ == "__main__":
    myApp.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  ## REMOVE THIS
    )
