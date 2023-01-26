from flask import Flask, render_template
import csv

app = Flask(__name__)

# args and kwargs in python

@app.route("/")
def index():
    num = 0
    with open("data/users.csv") as file:
        for line in file:
            num = num + 1

    return render_template("index.html",
        number_of_users=num,
        user_id="Z848989EBKZXC90B")


@app.route("/users/<user_id>")
def user_info(user_id):
    with open("data/users.csv") as file:
        found_user = None
        reader = csv.reader(file)
        for user in reader:
            if user[0] == user_id:
                found_user = user

        return render_template("user.html", user=found_user)        

        



@app.route("/about")
def about():
    return render_template("about.html")


app.run(port=8080, debug=True)