from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/profile'>press here</a> "

@app.route("/profile")
def profile():
    return "you r in profile section"



if __name__ == "__main__":
    app.run(debug=True)



