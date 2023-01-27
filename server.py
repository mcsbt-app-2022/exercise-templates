from flask import Flask, render_template
import csv

app = Flask(__name__)

# args and kwargs in python

@app.route("/")
def index():
    num = 0
    list_of_users = []
    with open("data/users.csv") as file:
        reader = csv.reader(file)
        for line in reader:
            list_of_users.append(line)
            num = num + 1

    return render_template("index.html",
        number_of_users=num,
        users=list_of_users)


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