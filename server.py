from flask import Flask, render_template, request, session, redirect
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "some secret string"

# args and kwargs in python

@app.route("/")
def index():
    if "username" in session:
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
    else:
        return redirect("/login")


@app.route("/users/<user_id>")
def user_info(user_id):
    with open("data/users.csv") as file:
        found_user = None
        reader = csv.reader(file)
        for user in reader:
            if user[0] == user_id:
                found_user = user

        return render_template("user.html", user=found_user)        

        
@app.route("/login")
def login_form():
    if "username" in session:
        return redirect("/")
    return render_template("login.html")


auth_db = {
    "pepe": "ilovepython",
    "diego": "slothsarecool",
}



@app.route("/handle-login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    if username in auth_db and auth_db[username] == password:
        session["username"] = username
        return redirect("/")
    else:
        return redirect("/login")




@app.route("/about")
def about():
    return render_template("about.html")


app.run(port=8080, debug=True)