from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/insert")
def profile():
    return render_template("insert.html")

@app.route("/insertmovie",methods=['POST'])
def insertmovie():
    # inserting the movies details in the cassandra database
    name=request.form['mname'];

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)




