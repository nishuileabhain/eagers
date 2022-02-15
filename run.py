import os  #  module for modifying directories
import json
from flask import Flask, render_template  # import Flask class from flask module

myApp = Flask(__name__)


@myApp.route("/")  # decorator which wraps functions
def index():
    return render_template("index.html")


@myApp.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])

#  can i say active is true for a given page? Do i want to?
@myApp.route("/contact")
def contact():
    data = []
    with open("data/tricks.json", "r") as my_json_data:
        data = json.load(my_json_data)
    return render_template("contact.html", page_title="Contact", tricks=data)


if __name__ == "__main__":
    myApp.run(
        host=os.environ.get("IP", "0.0.0.0"),  #default values
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # REMOVE THIS
    )
