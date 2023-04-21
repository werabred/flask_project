from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<b>hello friend!</b>"

@app.route("/greetings/")
def hello_python():
	return "<html lang=\"en\"><head>What holiday is it?</head><body><p><a href=\"/greetings/christmas\">it's christmas</a></p><p><a href=\"/greetings/newyear\">it's the new year</a></p></body></html>"

@app.route("/greetings/<name>")
def hello_user(name):
	if name == "christmas":
		return redirect(url_for("christmas"))
	elif name == 'newyear':
		return redirect(url_for("newyear")) #function name?
	else:
		return redirect(url_for("error"))


@app.route("/greetings/christmas")
def christmas():
	return "<b>merry christmas</b>"

@app.route("/greetings/newyear")
def newyear():
	return "<b>happy new year!</b>"

@app.route("/greetings/error")
def error():
	return "sorry that wasnt the new year or christmas!"

if __name__ == "__main__":
	app.run()
