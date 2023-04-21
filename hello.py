from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello <b>World</b>"

@app.route("/python")
def hello_python():
    return "Hello Python"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest = name))

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello {0} as Guest".format(guest)

if __name__ == "__main__":
    app.run()
