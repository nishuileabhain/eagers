import os  #  module for modifying directories
from flask import Flask, render_template  # import Flask class from flask module

myApp = Flask(__name__)


@myApp.route("/")  # decorator which wraps functions
def index():
    return render_template("index.html")


@myApp.route("/about")
def about():
    return render_template("about.html", page_title="About")

#  can i say active is true for a given page? Do i want to?
@myApp.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    myApp.run(
        host=os.environ.get("IP", "0.0.0.0"),  #default values
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # REMOVE THIS
    )
