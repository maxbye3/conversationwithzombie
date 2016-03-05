from flask import Flask
app = Flask(__name__)



@app.route("/hello")
def hello():
	return "helloww"

@app.route("/hello/to")
def hi():
	return "asd"





if __name__ == "__main__":
	app.run(debug=True)